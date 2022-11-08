from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User ,auth
from django.urls import reverse
from web.models import Web_Challenges_solve


# Create your views here.
def home(request):
    return render(request,'landing.html')
    #return HttpResponse("THIS IS LANDING PAGE")

def logout_function(request):
    logout(request)
    return HttpResponseRedirect(reverse(home))


@login_required(login_url="login/")
def community(request):
    return render(request,'community.html')
    #return HttpResponse("THIS IS COMMUNITY PAGE")


@login_required(login_url="login/")
def challenges(request):
    return render(request,'challenges.html')
    #return HttpResponse("THIS IS CHALLENGES PAGE")



@login_required(login_url="login/")
def scoreboard(request):
    

    return render(request,'scoreboard.html')
    #return HttpResponse("THIS IS SCOREBOARD PAGE")



@login_required(login_url="login/")
def myprofile(request):
    if request.method=='POST':
        if User.objects.filter(username=request.user.username).exists():
            firstname=request.POST['firstname']
            mobile=request.POST['mobile']
            request.user.last_name=mobile
            request.user.first_name=firstname
            request.user.save()
        
    context={}
    # context['user']=request.user
    # obj=Web_Challenges_solved.objects.all().filter(Username=context['user'] )
    # count=0
    # for x in obj :
    #     count+=1
    # print(count)

    
    return render(request,'pro.html')
    

@login_required(login_url="login/")
def faq(request):
    return render(request,'faq.html')
