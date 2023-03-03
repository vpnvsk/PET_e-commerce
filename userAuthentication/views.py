from django.shortcuts import render, redirect
from .forms import SignupForm 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

def log_out(request):
    logout(request)
    messages.info(request,'Logged out successfully!')
    return redirect('.')
