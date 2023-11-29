from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path('',views.welcomePage,name='welcomePage'),
    
    path('user/',views.welcomePage,name='welcomePage'),

    path('admin/',views.loginAdmin,name='admin'),
    path('admin/registerUser/',views.registerUser,name='registerUser'),
    path('admin/registerUser/registerUserSubmit',views.registerUserSubmit,name='registerUserSubmit'),
]