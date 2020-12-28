from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'{username} accout created successfully')
            return redirect('/login')
    else:
        form=UserRegisterForm()

    return render(request,'register.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        p_form= ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request,f'Changes has been updated')
            return redirect('/profile/')
        
    else:
        p_form= ProfileUpdateForm(instance=request.user.profile)   
    context={ 
            'p_form':p_form
        }
    return render(request,'profile.html',context)

