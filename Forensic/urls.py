from django.urls import path,include

from . import views


urlpatterns = [
    path('',views.Forensics ),
    path('<str:Challengeid_fc>/',views.solve_interface,name='solveid5'),
]