from django.shortcuts import render
from django.views.generic.base import View
from .models import Products, Shoe_size



def indexPage(request):
    return render(request, 'index.html')



class ProductView(View):
    #main page
    def get(self, request):
        product_view = Products.objects.all()
        return render(request, 'index.html' , {'product_list':product_view})

class CertainProductView(View):
    #certain product
    def get(self, request, pk):
        product = Products.objects.get(id = pk)
        ssize = Shoe_size.objects.all()
        return render(request, 'productPage.html',{'product':product, 'ssize':ssize})
    
    
