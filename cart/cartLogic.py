from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from productsContent.models import Products
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Size, ProductSize
from django.db.models import F



def add_to_cart(request,size_id, pk):
            
                      
    item = get_object_or_404(Products, id=pk)
    
    size = Size.objects.filter(id=size_id).first()
    
    order_item, created = OrderItem.objects.get_or_create(
        product = item,
        size = size,
        is_ordered = False,
    )

    order_qs = Order.objects.filter(owner = request.user, is_ordered = False)

    if order_qs.exists():

        order = order_qs[0]
            # check if the order item is in the order
        if order.items.filter(product=item, size = size).exists():
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
    

@login_required     
def remove_item(request, pk):
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

   