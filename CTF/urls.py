from django.contrib import admin
from django.urls import path
from CTF import views

urlpatterns = [
    path("",views.home, name='PROJECT CTF'),
    path('logout',views.logout_function),
    path("community",views.community, name='Community'),
    path("scoreboard",views.scoreboard, name='Scoreboard'),
    path("challenges",views.challenges, name='Challenges'),
    path("myprofile",views.myprofile, name='PROFILE'),
    path("facts",views.faq,name='faq')
    
]
