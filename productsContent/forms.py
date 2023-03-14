from django import forms
from .models import Shoe_size


class Size_select_form(forms.Form):

    s = Shoe_size()
    _40 = s.f40
    _40_5 = s.f40d5
    _41 = s.f41
    _41_5 = s.f41d5
    _42 = s.f42
    _42_5 = s.f42d5
    _43 = s.f43
    _44 = s.f44
    _44_5 = s.f44d5    
    _45 = s.f45
    sizes = ((_40,'f40'),
             (_40_5,'f40d5'),
             (_41,'f41'),
             (_41_5,'f41d5'),
             (_42,'f42'),
             (_42_5,'f42d5'),
             (_43,'f43'),
             (_44,'f44'),
             (_44_5,'f44d5'),
             (_45,'f45')) 
    size = forms.ChoiceField(label='Size', widget=forms.Select,choices=sizes)