from django.shortcuts import redirect, render
from django.views.generic.base import View
from .models import Products, Shoe_size, Brand
from .forms import SignupForm 


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
        brands = Brand.objects.all()
        brand_id = request.GET.get('brand', 0)

        if brand_id:
            product_view = product_view.filter(brand=brand_id)
        return render(request, 'productPage.html',{
            'product':product,            
            'brands': brands,
            'brand_id':int(brand_id)
            })
    



def sigup( request):

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
            
    else:
        form = SignupForm()

    return render(request, 'signup.html',{
        'form': form
    })

