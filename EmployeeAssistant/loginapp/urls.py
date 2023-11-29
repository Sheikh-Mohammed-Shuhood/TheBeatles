from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path('',views.welcomePage,name='welcomePage'),
    path('admin',views.welcomePage,name='welcomePage'),
    path('user',views.welcomePage,name='welcomePage'),
]