from django.urls import path
from . import views
urlpatterns=[
    path('',views.reverse),
    path('<str:Challengeid_rev>/',views.solve_interface,name='solveid2'),
]
