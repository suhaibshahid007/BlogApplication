from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import  login_required

from .forms import UserLoginForm , UserRegisterForm

from django.contrib.auth import (
               authenticate,
               login,
               logout,
      )

# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/posts/list")
    title ="Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form .cleaned_data.get("password")
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request , user)
            return HttpResponseRedirect("/posts/list/")





    context = {
             "form" : form,
             "title" : title,
    }
    return render (request , "login_form.html" , context)

def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user =authenticate(username = user.username , password = password)
        login(request , new_user)
        # now redirect to the login page ..
        return HttpResponseRedirect("/posts/list/")




    context ={
        "form" : form,
        "title" : "Registeration",
    }
    return render(request , "register_form.html" , context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login/")