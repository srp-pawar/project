from django.urls import path
from . import views
urlpatterns=[
    path('',views.misc),
    path('<str:Challengeid_mc>/',views.solve_interface,name='solveid3'),
]
