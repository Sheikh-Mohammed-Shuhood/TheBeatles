from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template import loader
from . import models
# from firebase_admin import auth


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

def loginAdmin(request):
    return render(request,"loginapp/dashboard.html")

def registerUser(request):
    return render(request,"loginapp/registerUser.html")



def send_verification_email(user):
    try:
        authe.send_email_verification(user['idToken'])
        print("Verification email sent to", user['email'])
    except Exception as e:
        print("Error sending verification email:", e)



def registerUserSubmit(request):
    if request.method=='POST':
        fname=request.POST['fname']
        eid=request.POST['eid']
        phone=request.POST['phone']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        passwd=request.POST['passwd']
        try:
            user = authe.create_user_with_email_and_password(email, passwd)
            print("User created:", user)
            send_verification_email(user)
            print("pass")
            
        except Exception as e:
            print("fail")
            return redirect('admin')
    return redirect('admin')