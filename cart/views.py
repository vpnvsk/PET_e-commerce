from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from userAuthentication.models import Profile
from .models import Order,OrderItem
from productsContent.models import Products, Brand,ProductSize,Size
from django.contrib import messages
from .extra import generate_ref_code
from django.urls import reverse
from django.utils import timezone
from django.db.models import F
from productsContent.forms import SizeForm
from django.http import JsonResponse
from productsContent.views import CertainProductView
from django.views.generic import View


import datetime


def get_user_pending_order(request):

    user_profile = get_object_or_404(Profile, user = request.user)
    order =  Order.objects.filter(owner = user_profile, is_ordered = False)

    if order.exists():
        return order[0]
    
    return 0 

def get_checkout(request):
    #try:
        orders = Order.objects.filter(owner=request.user, is_ordered=False)

        brands = Brand.objects.all()
        brand_id = request.GET.get('brand', 0)

        if brand_id:
            product_view = product_view.filter(brand=brand_id)
                            
        return render(request, 'checkout.html', {
            'orders':orders,
            #'products':lst,
            'brands': brands,
            'brand_id':int(brand_id)
            })
    #except:
     #   messages.info(request, "You need to be loged in")
      #  return redirect("productsContent:index")

class AddToCartView(View):


    def post(self, request, pk):
        if request.method == 'POST':
            
            request_getdata = request.POST.get('size', None)
            
            item = get_object_or_404(Products, id=pk)
            for i in request_getdata:
                try:
                    size_id = int(i)
                except:
                    pass
            size = Size.objects.filter(id=size_id).first()
            print("took size")

            order_item, created = OrderItem.objects.get_or_create(
                product = item,
                size = size,
                is_ordered = False,
            )

            order_qs = Order.objects.filter(owner = request.user, is_ordered = False)
            if order_qs.exists():
                print('in first if')
                order = order_qs[0]
                    # check if the order item is in the order
                if order.items.filter(product=item, size = size).exists():
                    print('order exist')
                    order_item.quantity = order_item.quantity + 1
                    order_item.save()
                    print('order saved')
                    messages.info(request, "This item quantity was updated.")
                    print('message send')
                    ProductSize.objects.filter( product = item ).update(count=F('count')-1)

                    return redirect("cart:checkout")
                else:
                    print('order doest exist')
                    order.items.add(order_item)
                    messages.info(request, "This item was added to your cart.")
                    print('message send')
                    ProductSize.objects.filter( product = item ).update(count=F('count')-1)

                    return redirect("cart:checkout")
            else:
                print('creating order')
                ordered_date = timezone.now()
                order = Order.objects.create(
                    owner=request.user, date_ordered=ordered_date)
                order.items.add(order_item)
                print('before message')
                messages.info(request, "This item was added to your cart.")
                print('message send')
                ProductSize.objects.filter( product = item ).update(count=F('count')-1)

                return redirect("productsContent:certain_product",pk=item.id)

            
    


    # @login_required
    # def add_to_cart(self, request, pk):
        
    #     ii = post(self, request, pk)
    #     item = get_object_or_404(Products, id=pk)
    #     size_ = Size.objects.filter(id = ii).first()
    #     i = ProductSize.objects.filter( product = item ).update(count=F('count')-1)
        
        
    #     order_item, created = OrderItem.objects.get_or_create(
    #         product=item,
    #         size = size_,
    #         is_ordered=False
    #         )
        
    #     order_qs = Order.objects.filter(owner=request.user, is_ordered=False)
    #     if order_qs.exists():
                
    #         order = order_qs[0]
    #             # check if the order item is in the order
    #         if order.items.filter(product__id=item.id).exists():
    #             order_item.quantity = order_item.quantity + 1
    #             order_item.save()
    #             messages.info(request, "This item quantity was updated.")
    #             return redirect("productsContent:certain_product",pk=item.id)
    #         else:
    #             order.items.add(order_item)
    #             messages.info(request, "This item was added to your cart.")
    #             return redirect("productsContent:certain_product",pk=item.id)
    #     else:
    #         ordered_date = timezone.now()
    #         order = Order.objects.create(
    #             owner=request.user, date_ordered=ordered_date)
    #         order.items.add(order_item)
    #         messages.info(request, "This item was added to your cart.")
    #         return redirect("productsContent:certain_product",pk=item.id)
        
    
        




@login_required
def order_details(request, **kwargs):

    existing_order = get_user_pending_order(request)

    return render(request, 'cart.html',{'existing_order':existing_order})





@login_required
def updete_transaction_records(request,order_id):

    order_to_purchase = Order.objects.filter(pk=order_id).first()

    order_to_purchase.is_ordered = True
    order_to_purchase.date_ordered = datetime.datetime.now()
    order_to_purchase.save()

    order_items = order_to_purchase.items.all()
    order_items.update(is_ordered=True, date_ordered = datetime.datetime.now())

    user_profile = get_object_or_404(Profile, user = request.user)

    order_products = [item.product for item in order_items]
    user_profile.prod.add(*order_products)
    user_profile.save()

    messages.info(request, 'Thank you')

    return redirect('/')




@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Products, id=pk)
    order_qs = Order.objects.filter(
        owner=request.user,
        is_ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(product__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                product=item,
                is_ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("cart:checkout")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("cart:checkout")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("cart:checkout")
