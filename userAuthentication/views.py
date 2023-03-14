from django.shortcuts import render, redirect
from .forms import SignupForm 
from django.contrib.auth import logout
from django.contrib import messages

from .models import Profile
from cart.models import Order


def sigup(request):

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

def log_out(request):
    logout(request)
    messages.info(request,'Logged out successfully!')
    return redirect('.')

def my_profile(request):
    my_user_profile = Profile.objects.filter(user = request.user).first()
    my_order = Order.objects.filter(owner = my_user_profile, is_ordered = True)

    return render(request, 'cart.html', {'my_order': my_order})
