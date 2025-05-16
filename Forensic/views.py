from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from logindemo import views
from django.contrib import auth
from .models import Forensics_challenges as fc,Forensics_challenges_solved

# Create your views here.
@login_required(login_url=views.login_function)
def Forensics(request):
    challenges=fc.objects.all()
    return render(request,'forensics.html',{'challenges':challenges})
    #return HttpResponse("THIS IS Forensic CHALLENGES PAGE")

def solve_interface(request,Challengeid_fc):
    object1=fc.objects.get(pk=Challengeid_fc)
    if request.method=='POST':
        flag1=request.POST['flag1']
        print(flag1)
        if flag1==object1.Challenge_Answer:
            solve_save=Forensics_challenges_solved(Username=request.user.username,Challenge_id=Challengeid_fc)
            solve_save.save()
            return HttpResponse('your anser is correct')
        else:
            return HttpResponse('your anser is wrong')
    return render(request, "solvefc.html",{'obj1':object1})