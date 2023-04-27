from django.shortcuts import  render
from django.views.generic.base import View
from .models import Products, Brand, ProductSize
from django.views.generic import View
from .forms import SizeForm
from django.http import JsonResponse



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
        
        item = Products.objects.get(id=pk)
        
        size = ProductSize.objects.filter( product = item, count__gt = 0 )

        form = SizeForm()
        
            
        product_qs = Products.objects.filter(id = pk)

        if product_qs.exists():

            product = product_qs[0]

            product_size_qs = ProductSize.objects.filter(product = product)
                            
            brands = Brand.objects.all()
            brand_id = request.GET.get('brand', 0)

            if brand_id:
                product_view = product_view.filter(brand=brand_id)
            return render(request, 'productPage.html',{
                'product':product,            
                'brands': brands,
                'brand_id':int(brand_id),
                'product_size': product_size_qs,
                'form':form            
                })
    def post(self, request, pk):
        
        if request.method == 'POST':
        # no need to do this
        # request_csrf_token = request.POST.get('csrfmiddlewaretoken', '')
            request_getdata = request.POST.get('size', None) 
            # make sure that you serialise "request_getdata" 
            return JsonResponse(request_getdata,safe = False) 
    
    


