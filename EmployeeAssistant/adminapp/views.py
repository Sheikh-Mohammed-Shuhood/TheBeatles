from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template import loader
from . import models
import pyrebase


# Create your views here.

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


empTrack = {
            "apiKey": "AIzaSyB8ArVGllljFel0S4DaAHhEsZeWnRKv0Jk",
            "authDomain": "storeactions-bdf68.firebaseapp.com",
            "databaseURL": "https://storeactions-bdf68-default-rtdb.firebaseio.com/",
            "projectId": "storeactions-bdf68",
            "storageBucket": "storeactions-bdf68.appspot.com",
            "messagingSenderId": "383468636556",
            "appId": "1:383468636556:web:f87bd60fc7c1b9bc7faea9",
            "measurementId": "G-BCCER9PMS8"
        };
empTrackFirebase = pyrebase.initialize_app(empTrack)
empTrackAuthe = empTrackFirebase.auth()
empTrackDatabase = empTrackFirebase.database()


def adminDashboard(request):
    print("-----------------------------------------------------------------")
    empList = []
    employees = empTrackDatabase.get().val()

    if(employees):
        for i in employees:
            empList.append(str(i))

    context = {
        "empList":empList,
    }

    print("-----------------------------------------------------------------")
    template=loader.get_template("adminapp/dashboard.html")
    return HttpResponse(template.render(context,request))


def trackEmpDetail(request,emp):
    print("-----------------------------------------------------------------")
    employee_data = empTrackDatabase.child(emp).get().val()
    print(employee_data)

    keyboard_key = 0
    mouse_key = 0
    process_value = 0
    time_value = 0
    browser_data = 0

    browsDict = dict()
    try:
        keyboard_key = employee_data['keyboardkey']
        mouse_key = employee_data['mousekey']
        process_value = employee_data['process']
        time_value = employee_data['time']
    except:
        print("keys not there")


    browser_data =empTrackDatabase.child(emp).child("browser").get().val()

    print("keyboard_key=",keyboard_key,"mouse_key=",mouse_key,"process_value=",process_value,"time_value=",time_value)


    if(browser_data):
        for browsKey,browsVal in browser_data.items():
            print(browsKey,browsVal)
            browsDict[str(browsKey)] = browsVal

    context = {
        'name':emp,
        'keyboard_key':keyboard_key,
        'mouse_key':mouse_key,
        'process_value':process_value,
        'time_value':time_value,
        'browser_data':browser_data,
        'browsDict':browsDict,
    }


    print("-----------------------------------------------------------------")
    template=loader.get_template("adminapp/trackEmployee.html")
    return HttpResponse(template.render(context,request))




    

def registerUser(request):
    return render(request,"adminapp/registerUser.html")



def send_verification_email(user):
    try:
        authe.send_email_verification(user['idToken'])
        print("Verification email sent to", user['email'])
    except Exception as e:
        print("Error sending verification email:", e)



def registerUserSubmit(request):
    print("-----------------------------------------------------------------")
    if request.method=='POST':
        fname=request.POST['fname']
        eid=request.POST['eid']
        phone=request.POST['phone']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        passwd=request.POST['passwd']

        userData = {
            "name":fname,
            "eid":eid,
            "phone":phone,
            "email":email,
            "age":age,
            "gender":gender,
            }
        

        try:
            user = authe.create_user_with_email_and_password(email, passwd)
            database.child("users").child(user['localId']).set(userData)
            
            retrieved_user_details = database.child('users').child(user['localId']).get().val()
            print("\n\n",retrieved_user_details['email'],"\n\n")

            print("User created:", user)
            send_verification_email(user)
            messages.success(request,f"successfully logged in as {user['email']}")
            print("pass")
        except Exception as e:
            print("fail")
            messages.error(request,f"failed to login")
            # return redirect('dashboard')
    print("-----------------------------------------------------------------")

    return redirect('adminDashboard')