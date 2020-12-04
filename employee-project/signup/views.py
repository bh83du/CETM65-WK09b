from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from signup.models import Users


def test(request):
    return HttpResponse("Congratulations. You found the Test page")

def index(request):
    return HttpResponse("This is the Index Page")

def signup(request):

    if request.method == "POST":

        details = {}

        details['emp_no'] = request.POST.get('emp_no','')
        details['user_name'] = request.POST.get('user_name','')
        details['dept'] = request.POST.get('dept','')
        details['email'] = request.POST.get('email','')
        details['password'] = request.POST.get('password','')

        print(details)

        new_user = Users(emp_no=details["emp_no"],
                         user_name=details["user_name"],
                         dept=details["dept"],
                         email=details["email"],
                         password=details["password"])

        print(new_user)

        new_user.save()

        return redirect('/')

    return render(request, "sign-up.html")

