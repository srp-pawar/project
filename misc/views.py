from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from logindemo import views
from django.contrib import auth
from .models import Misc_challenges as mc
from .models import Misc_challenges_solved

# Create your views here.
@login_required(login_url=views.login_function)
def misc(request):
    challenges=mc.objects.all()
    return render(request,'misc.html',{'challenges':challenges})
    #return HttpResponse("THIS IS web CHALLENGES PAGE")

def solve_interface(request,Challengeid_mc):
    object1=mc.objects.get(pk=Challengeid_mc)
    if request.method=='POST':
        flag3=request.POST['flag3']
        print(flag3)
        if flag3==object1.Challenge_Answer:
            solve_save=Misc_challenges_solved(Username=request.user.username,Challenge_id=Challengeid_mc)
            solve_save.save()
            return HttpResponse('your answer is correct')
        else:
            return HttpResponse('your anser is wrong')
    return render(request, "solvemisc.html",{'obj2':object1})