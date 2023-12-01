from django.contrib import admin
from django.urls import include,path
from . import views


urlpatterns = [
    path('',views.employeeDashboard,name='employeeDashboard'),
    path('query/querySubmit',views.querySubmit,name='querySubmit'),

    path('feed/',views.feed,name='feed'),
    path('query/',views.query,name='query'),
    path('unanswered/',views.unanswered,name='unanswered'),
    path('finance/',views.finance,name='Finance'),
    path('marketing/',views.marketing,name='Marketing'),
    path('analyst/',views.analyst,name='Analyst'),
    path('devop/',views.devop,name='Devop'),

    path('answerSubmit',views.answerSubmit,name='answerSubmit'),
    path('answering/<str:question>/<str:dept>',views.answering,name='answering'),

    
]