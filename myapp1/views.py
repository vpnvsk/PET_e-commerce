from django.shortcuts import render
from django.views.generic.base import View
from .models import Products, Shoe_size, Brand



def indexPage(request):
    return render(request, 'index.html')



class ProductView(View):
    #main page
    def get(self, request):

        product_view = Products.objects.all()
        brands = Brand.objects.all()
        brand_id = request.GET.get('brand', 0)

        if brand_id:
            product_view = product_view.filter(brand=brand_id)

        return render(request, 'index.html' , {
            'product_list':product_view,
            'brands': brands,
            'brand_id':int(brand_id)
            })
    


class CertainProductView(View):
    #certain product
    def get(self, request, pk):
        product = Products.objects.get(id = pk)
        ssize = Shoe_size.objects.all()
        return render(request, 'productPage.html',{'product':product, 'ssize':ssize})
    
    
