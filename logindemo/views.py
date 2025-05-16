from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login ,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from landpage import views
# Create your views here.
def login_function(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password1']
        user=auth.authenticate(username=username, password=password)
        if user is None:
            messages.error(request,'INVALID LOGIN CREDENTIALS')
            return redirect('/login')
        else:
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:    
                return HttpResponseRedirect(reverse(views.index))

    return render(request,'loginfile.html')