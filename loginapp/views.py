import json
import requests
from django.shortcuts import render


# Create your views here.
def regis(request):
    return render(request, 'register.html')


def index(request, text = {
    "text": "Hello world",
}):
    return render(request, 'index.html', text)


def login(request):
    return render(request, 'login.html', {"text": ""})


def info(request):
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    # validation
    if username == "" or password1 == "" or password2 == "":
        return render(request, 'register.html', {
            "text": "Fields cannot be empty."
            })
    if password1 != password2:
        return render(request, 'register.html', {
            "text": "Password not match."
        })

    # api
    p = {
        "username": f"{username}",
        "password": f"{password1}",
    }
    payload = json.dumps(p)
    r = requests.post("http://localhost:8000/api/register/", payload)
    if r.json()['status_code']:
        return render(request, 'register.html',{
            "text": "Username already exists"
        })
    return render(request, 'login.html')


def login_validate(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        r = requests.get("http://localhost:8000/api/auth", {
            'u_name': username,
            'pwd': password,
        })
        if r.json()['password'] == '':
            return render(request, 'login.html', {'text': 'Wrong password'})
    except json.JSONDecodeError:
        return render(request, 'login.html', {'text': 'Username not found'})
    account = requests.get("http://localhost:8000/api/profile", {'u_name': username})
    return render(request, 'profile.html', account.json()[0])


def edit(request):
    account = requests.get(
        "http://localhost:8000/api/profile",
        {
            'u_name': request.POST['username']
        }
    )
    print(account.json()[0])
    return render(request, 'edit.html', account.json()[0])


def submit(request):
    account = {
        "username": request.POST['username'],
        "firstname": request.POST['firstname'],
        "lastname": request.POST['lastname'],
        "email": request.POST['email'],
        "tel_number": request.POST['tel_number'],
    }
    print(account)
    return render(request, 'login.html')
