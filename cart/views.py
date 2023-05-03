from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from .models import Order
from productsContent.models import Products, Brand
from .cartLogic import add_to_cart, remove_item


def get_checkout(request):
        orders = Order.objects.filter(owner=request.user, is_ordered=False)

        brands = Brand.objects.all()
        brand_id = request.GET.get('brand', 0)

        if brand_id:
            product_view = product_view.filter(brand=brand_id)
                            
        return render(request, 'checkout.html', {
            'orders':orders,
            'brands': brands,
            'brand_id':int(brand_id)
            })


class AddToCartView(View):


    def post(self, request, pk):
        if request.method == 'POST':
            item = get_object_or_404(Products, id=pk)

            request_getdata = request.POST.get('size', None)
            
            for i in request_getdata:
                try:
                    size_id = int(i)
                except:
                    pass

            add_to_cart(request, size_id, pk)
        return redirect("productsContent:certain_product",pk=item.id)

                 
# @login_required
# def updete_transaction_records(request,order_id):

#     order_to_purchase = Order.objects.filter(pk=order_id).first()

#     order_to_purchase.is_ordered = True
#     order_to_purchase.date_ordered = datetime.datetime.now()
#     order_to_purchase.save()

#     order_items = order_to_purchase.items.all()
#     order_items.update(is_ordered=True, date_ordered = datetime.datetime.now())

#     user_profile = get_object_or_404(Profile, user = request.user)

#     order_products = [item.product for item in order_items]
#     user_profile.prod.add(*order_products)
#     user_profile.save()

#     messages.info(request, 'Thank you')

#     return redirect('/')




@login_required
def remove_from_cart(request, pk):

    remove_item(request,pk)
    return redirect("cart:checkout")
