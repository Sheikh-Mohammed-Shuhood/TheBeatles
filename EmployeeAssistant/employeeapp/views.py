from django.shortcuts import render,redirect
import pyrebase
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader



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
        userEmail = request.session.get('user_email')
        print(userEmail)

        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

        userData = {
            "user":userEmail,
            "time":formatted_time,
            "query":query
        }

        try:
            database.child(str(dept)).child('question').child(str(query)).set(userData)
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
    fin_ref = database.child("Finance")
    questions_data = fin_ref.child("question").get().val()
    questionsListFinance = []

    if questions_data:
    # Process each question
        for question_key, question_data in questions_data.items():
            query = question_data.get("query")
            answer = question_data.get("answer")

            if(answer):
                continue

            print(f"Query: {query}")

            question_dict = {
            "question": question_key,
            "query": query,
            }

            questionsListFinance.append(question_dict)
    else:
        print("No data found under")

    print(questionsListFinance)

    context={
        'queriesFinance':questionsListFinance,
    }

    template=loader.get_template("employeeapp/unanswered.html")
    return HttpResponse(template.render(context,request))
    # return render(request,"employeeapp/unanswered.html")



def finance(request):
    fin_ref = database.child("Finance")
    questions_data = fin_ref.child("question").get().val()
    print(questions_data)

    questions_list = []

    if questions_data:
    # Process each question
        for question_key, question_data in questions_data.items():
            print(f"Question: {question_key}")

            # Extract details for each question
            query = question_data.get("query")
            user = question_data.get("user")
            time = question_data.get("time")

            answer = question_data.get("answer")

            if(answer):
                answerUser = question_data.get("answerUser")
                answerTime = question_data.get("answerTime")
                print(f"answer: {answer}")
                print(f"answer User: {answerUser}")
                print(f"answer Time: {answerTime}")
            else:
                continue

            print(f"Query: {query}")
            print(f"User: {user}")
            print(f"Time: {time}")
            print("-" * 20)

            question_dict = {
            "question": question_key,
            "query": query,
            "user": user,
            "time": time,
            "answer": answer,
            "answerUser": answerUser,
            "answerTime": answerTime
            }

            questions_list.append(question_dict)
    else:
        print("No data found under")

    print(questions_list)

    context={
        'queries':questions_list,
    }

    template=loader.get_template("employeeapp/finance.html")
    return HttpResponse(template.render(context,request))


def marketing(request):
    market_ref = database.child("Marketing")
    questions_data = market_ref.child("question").get().val()
    print(questions_data)

    questions_list = []

    if questions_data:
    # Process each question
        for question_key, question_data in questions_data.items():
            print(f"Question: {question_key}")

            # Extract details for each question
            query = question_data.get("query")
            user = question_data.get("user")
            time = question_data.get("time")

            answer = question_data.get("answer")

            if(answer):
                answerUser = question_data.get("answerUser")
                answerTime = question_data.get("answerTime")
                print(f"answer: {answer}")
                print(f"answer User: {answerUser}")
                print(f"answer Time: {answerTime}")
            else:
                continue

            print(f"Query: {query}")
            print(f"User: {user}")
            print(f"Time: {time}")
            print("-" * 20)

            question_dict = {
            "question": question_key,
            "query": query,
            "user": user,
            "time": time,
            "answer": answer,
            "answerUser": answerUser,
            "answerTime": answerTime
            }

            questions_list.append(question_dict)
    else:
        print("No data found under")

    print(questions_list)

    context={
        'queries':questions_list,
    }

    template=loader.get_template("employeeapp/finance.html")
    return HttpResponse(template.render(context,request))

def analyst(request):
    analyst_ref = database.child("Analyst")
    questions_data = analyst_ref.child("question").get().val()
    print(questions_data)

    questions_list = []

    if questions_data:
    # Process each question
        for question_key, question_data in questions_data.items():
            print(f"Question: {question_key}")

            # Extract details for each question
            query = question_data.get("query")
            user = question_data.get("user")
            time = question_data.get("time")

            answer = question_data.get("answer")

            if(answer):
                answerUser = question_data.get("answerUser")
                answerTime = question_data.get("answerTime")
                print(f"answer: {answer}")
                print(f"answer User: {answerUser}")
                print(f"answer Time: {answerTime}")
            else:
                continue

            print(f"Query: {query}")
            print(f"User: {user}")
            print(f"Time: {time}")
            print("-" * 20)

            question_dict = {
            "question": question_key,
            "query": query,
            "user": user,
            "time": time,
            "answer": answer,
            "answerUser": answerUser,
            "answerTime": answerTime
            }

            questions_list.append(question_dict)
    else:
        print("No data found under")

    print(questions_list)

    context={
        'queries':questions_list,
    }

    template=loader.get_template("employeeapp/finance.html")
    return HttpResponse(template.render(context,request))



def devop(request):
    devop_ref = database.child("Devop")
    questions_data = devop_ref.child("question").get().val()
    print(questions_data)

    questions_list = []

    if questions_data:
    # Process each question
        for question_key, question_data in questions_data.items():
            print(f"Question: {question_key}")

            # Extract details for each question
            query = question_data.get("query")
            user = question_data.get("user")
            time = question_data.get("time")

            answer = question_data.get("answer")

            if(answer):
                answerUser = question_data.get("answerUser")
                answerTime = question_data.get("answerTime")
                print(f"answer: {answer}")
                print(f"answer User: {answerUser}")
                print(f"answer Time: {answerTime}")
            else:
                continue

            print(f"Query: {query}")
            print(f"User: {user}")
            print(f"Time: {time}")
            print("-" * 20)

            question_dict = {
            "question": question_key,
            "query": query,
            "user": user,
            "time": time,
            "answer": answer,
            "answerUser": answerUser,
            "answerTime": answerTime
            }

            questions_list.append(question_dict)
    else:
        print("No data found under")

    print(questions_list)

    context={
        'queries':questions_list,
    }

    template=loader.get_template("employeeapp/finance.html")
    return HttpResponse(template.render(context,request))



def answering(request):
    return render(request,"employeeapp/answering.html")


def answerSubmit(request):
    if(request.method == 'POST'):
        answer = request.POST['answer']
        userEmail = request.session.pop('user_email', None)
        print(userEmail)

        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

        userData = {
            "user":userEmail,
            "time":formatted_time,
            "answer":answer
        }
    pass
    #     try:
    #         database.child(str(dept)).child('question').child(str(query)).set(userData)
    #         messages.success(request,f"successfully stored the query {query}")
    #         print("successfully stored the query")
    #     except:
    #         print("cant store the query")
    #         messages.error(request,f"failed to store query")
    # return redirect('employeeDashboard')