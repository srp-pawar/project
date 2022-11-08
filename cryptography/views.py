from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from logindemo import views
from django.http import HttpResponseRedirect

from django.contrib import auth
from .models import Cryptography_Challenges as cc,Cryptography_Challenges_solved
from django.urls import reverse
from django.contrib import messages


# Create your views here.
@login_required(login_url=views.login_function)
def cryptography(request):
    challenges=cc.objects.all()
    return render(request,'crypto.html',{'challenges':challenges})
    #return HttpResponse("THIS IS web CHALLENGES PAGE")

def solve_interface(request,Challengeid_cc):
    object1=cc.objects.get(pk=Challengeid_cc)
    if request.method=='POST':
        flag=request.POST['flag']
        print(flag)
        if flag==object1.Challenge_Answer:
            solve_save=Cryptography_Challenges_solved(Username=request.user.username,Challenge_id=Challengeid_cc)
            solve_save.save()
            return HttpResponse('your anser is correct')
        else:
            return HttpResponse('your anser is wrong')
            
    return render(request, "solvecrypto.html",{'obj2':object1})
