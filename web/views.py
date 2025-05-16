from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from logindemo import views
from django.contrib import auth
from .models import Web_Challenges as wc
from .models import Web_Challenges_solved 

# Create your views here.
@login_required(login_url=views.login_function)
def web(request):
    challenges=wc.objects.all()
    return render(request,'web.html',{'challenges':challenges})
    #return HttpResponse("THIS IS web CHALLENGES PAGE")

def solve_interface(request,Challengeid_web):
    object1=wc.objects.get(pk=Challengeid_web)
    if request.method=='POST':
        flag6=request.POST['flag6']
        print(flag6)
        if flag6==object1.Challenge_Answer:
            solve_save=Web_Challenges_solved(Username=request.user.username,Challenge_id=Challengeid_web)
            solve_save.save()
            return HttpResponse('your answer is correct')
        else:
            return HttpResponse('your answer is wrong')
    return render(request, "solve.html",{'obj2':object1})