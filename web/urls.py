from django.urls import path
from . import views
urlpatterns=[
    path('',views.web),
    path('<str:Challengeid_web>/',views.solve_interface,name='solveid1'),
]
