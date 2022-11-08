from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from logindemo import views
from django.contrib import auth
from .models import ReverseEngineering_challenges as rc
from .models import ReverseEngineering_challenges_solved
# Create your views here.
@login_required(login_url=views.login_function)
def reverse(request):
    challenges=rc.objects.all()
    return render(request,'rev.html',{'challenges':challenges})
    #return HttpResponse("THIS IS web CHALLENGES PAGE")

def solve_interface(request,Challengeid_rev):
    object1=rc.objects.get(pk=Challengeid_rev)
    if request.method=='POST':
        flag4=request.POST['flag4']
        print(flag4)
        if flag4==object1.Challenge_Answer:
            solve_save=ReverseEngineering_challenges_solved(Username=request.user.username,Challenge_id=Challengeid_rev)
            solve_save.save()
            return HttpResponse('your answer is correct')
        else:
            return HttpResponse('your answer is wrong')
    return render(request, "solverev.html",{'obj2':object1})