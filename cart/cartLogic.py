from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from productsContent.models import Products
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone



@login_required
def add_to_cart(request, pk):
    
    item = get_object_or_404(Products, id=pk)
    order_item, created = OrderItem.objects.get_or_create(
        product=item,            
        is_ordered=False
        )
    order_qs = Order.objects.filter(owner=request.user, is_ordered=False)
    if order_qs.exists():
            
        order = order_qs[0]
            # check if the order item is in the order
        if order.items.filter(product__id=item.id).exists():
            order_item.quantity = order_item.quantity + 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("productsContent:index")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("productsContent:index")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
        owner=request.user, date_ordered=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("productsContent:index")
   