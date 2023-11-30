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
    return render(request,"employeeapp/employeeDashboard.html")


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
