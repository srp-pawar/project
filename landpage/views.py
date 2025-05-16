from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.urls import reverse
from django.http import HttpResponse
from .models import Testimonials
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from logindemo import views
from django.contrib import auth
from django.contrib import messages
from .models import Messages_users
# Create your views here.

@login_required(login_url='/login') 
def index(request):
    if request.method=='POST':
        messagesbyx=request.POST['message']
        message_ref=Messages_users(Username=request.user.username,Email_id=request.user.email,message_by_user=messagesbyx)
        message_ref.save()
        messages.success(request,'Our Team  Will Contact U  soon within an hour please have patience')
        return redirect('/about#contact-us')

    appname='CTFPLAYS'
    testimonial_object= Testimonials.objects.all() 
    context={}
    context['user']=request.user
    return render(request,'index2.html',{'testimonial_object':testimonial_object,'appname':appname,'context':context})



    


