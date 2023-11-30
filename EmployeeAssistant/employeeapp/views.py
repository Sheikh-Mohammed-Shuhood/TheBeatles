from django.shortcuts import render,redirect
import pyrebase
from datetime import datetime
from django.contrib import messages


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
def employeeDashboard(request):
    return render(request,"employeeapp/index.html")


def querySubmit(request):
    if(request.method == 'POST'):
        dept = request.POST['department']
        query = request.POST['query']
        userEmail = request.session.pop('user_email', None)
        print(userEmail)

        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

        userData = {
            "user":userEmail,
            "time":formatted_time,
            "query":query
        }

        try:
            database.child(str(dept)).child(str(query)).set(userData)
            messages.success(request,f"successfully stored the query {query}")
            print("successfully stored the query")
        except:
            print("cant store the query")
            messages.error(request,f"failed to store query")
    return redirect('employeeDashboard')



def feed(request):
    return render(request,"employeeapp/feed.html")

def query(request):
    return render(request,"employeeapp/query.html")

def unanswered(request):
    return render(request,"employeeapp/unanswered.html")

def finance(request):
    return render(request,"employeeapp/finance.html")

def marketing(request):
    return render(request,"employeeapp/marketing.html")

def analyst(request):
    return render(request,"employeeapp/analyst.html")

def devop(request):
    return render(request,"employeeapp/devop.html")

def answering(request):
    return render(request,"employeeapp/answering.html")