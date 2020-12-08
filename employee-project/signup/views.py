from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from signup.models import Users


def test(request):
    # Easter Egg Test Page 
    return HttpResponse("Congratulations. You found the Test page")

def data(request):
    # This will return all records currently in the DB.
    all_users = Users.objects.all()
    return render(request, 'data.html', {'all_users': all_users,})

def signup(request):

    if request.method == "POST":

        details = {}

        details['emp_no'] = request.POST.get('emp_no','')
        details['user_name'] = request.POST.get('user_name','')
        details['dept'] = request.POST.get('dept','')
        details['email'] = request.POST.get('email','')
        details['password'] = request.POST.get('password','')

        print(details)

        missing = list()

        for k, v in details.items():
            if v == "":
                missing.append(k)

        if missing:
            messages.add_message(
                request, messages.WARNING, f"Missing fields for {', '.join(missing)}")
            return render(request, "signup.html")

        new_user = Users(emp_no=details["emp_no"],
                         user_name=details["user_name"],
                         dept=details["dept"],
                         email=details["email"],
                         password=details["password"])


        print(new_user)

        new_user.save()

        return redirect('/signup/data')

    return render(request, "signup.html")

