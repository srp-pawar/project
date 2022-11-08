from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User ,auth
from django.urls import reverse
from django.http import HttpResponseRedirect
from logindemo import views

# Create your views here.
def registerfunction(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.error(request,'USERNAME  ALREADY EXISTS')
            return redirect('/register')
        if User.objects.filter(email=email).exists():
            messages.error(request,'EMAIL ALREADY EXISTS')
            return redirect('/register')

        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            user=User.objects.create_user(username=username,email=email,password=password1)
            user.save()
            return HttpResponseRedirect(reverse(views.login_function))
        else:
            messages.error(request,'PASSWORD DIDNOT MATCH')
            return redirect('/register')

    return render(request,'registerfile.html')