from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template import loader
from . import models

import pyrebase

config = {
    "apiKey": "AIzaSyA8MCanCoi37ZieknWHnlYaqQWj0Nb2Vzk",
    "authDomain": "employee-assistant-38ef2.firebaseapp.com",
    "databaseURL":"https://employee-assistant-38ef2-default-rtdb.firebaseio.com/",
    "projectId": "employee-assistant-38ef2",
    "storageBucket": "employee-assistant-38ef2.appspot.com",
    "messagingSenderId": "73732843695",
    "appId": "1:73732843695:web:61a81bafa5882aebf50c5a"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()



# Create your views here.
def welcomePage(request):
    nm = database.child('Rathan').child('Name').get().val()
    print(nm)
    return render(request,"loginapp/index.html")

