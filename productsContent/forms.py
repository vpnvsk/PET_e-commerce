from django import forms
from productsContent.models import Size
from cart.models import OrderItem
from .models import Products, ProductSize



class SizeForm(forms.Form):


    size_field = forms.ModelChoiceField(
                queryset=Size.objects.all(),
                widget=forms.Select,
                empty_label="select size"
                                )
