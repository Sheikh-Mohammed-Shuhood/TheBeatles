from django.contrib import admin
from django.urls import include,path
from . import views


urlpatterns = [
    path('',views.adminDashboard,name='adminDashboard'),
    path('trackUser/<str:emp>',views.trackEmpDetail,name='trackEmpDetail'),
    path('registerUser/',views.registerUser,name='registerUser'),
    path('registerUser/registerUserSubmit',views.registerUserSubmit,name='registerUserSubmit'),

]