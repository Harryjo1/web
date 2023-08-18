from django.shortcuts import render, redirect
from .forms import UserRegisteration
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthorized_user


# Create your views here.
def home(request):    
    return render(request, 'userprofile/base.html')


# def userRegisteration(request):
#     form=UserRegisteration()
#     context={'form':form}
#     return render(request,'userprofile/register.html', context)

#@unauthorized_user
def userRegisteration(request):
    form=UserRegisteration()
    if request.method=='POST':
        print("In post Processing") # c'est moi qui est rajouté
        form=UserRegisteration(request.POST)
        print(form.instance) # c'est moi qui ai rajouté pour visualié les elements qu'on vient d'enregistre en base
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username') # "username nom de l'attribut de la class"
            messages.info(request, username + 'your account is created login to continue')
            return redirect('userprofile:login')

    context={'form':form}
    return render(request, 'userprofile/register.html', context)
#@unauthorized_user
def userLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('forum:home')
        else:
            messages.info(request,'usernam or password is incorrect')
        
    return render(request, 'userprofile/login.html')

def userLogout(request):
    return render(request, 'forum/index.html')


#@login_required(login_url='userprofile:login')
def profile(request):
    return render(request, 'userprofile/profile.html')









    