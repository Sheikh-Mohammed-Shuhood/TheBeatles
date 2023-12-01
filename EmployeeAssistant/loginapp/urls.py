from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path('',views.welcomePage,name='welcomePage'),
    
    # path('user/',views.welcomePage,name='welcomePage'),
    path('signinUserSubmit',views.signinUserSubmit,name='signinUserSubmit'),
    path('loginAdminSubmit',views.loginAdminSubmit,name='loginAdminSubmit'),
    # path('adminDashboard',views.adminDashboard,name='adminDashboard'),
    
]