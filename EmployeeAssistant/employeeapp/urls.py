from django.contrib import admin
from django.urls import include,path
from . import views


urlpatterns = [
    path('',views.employeeDashboard,name='employeeDashboard'),
    path('query/querySubmit',views.querySubmit,name='querySubmit'),

    path('feed/',views.feed,name='feed'),
    path('query/',views.query,name='query'),
    path('unanswered/',views.unanswered,name='unanswered'),
    path('finance/',views.finance,name='finance'),
    path('marketing/',views.marketing,name='marketing'),
    path('analyst/',views.analyst,name='analyst'),
    path('devop/',views.devop,name='devop'),
    path('answering/',views.answering,name='answering'),
]