
from django.urls import path
from . import views
urlpatterns=[
    path('',views.cryptography),
    path('<str:Challengeid_cc>/',views.solve_interface,name='solveid4'),
]
