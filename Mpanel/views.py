from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape


def index(request):
    return render(request, 'mpanel/home.html')


def login(request):
    if request.method == 'POST':

        login = escape(request.POST.get('login'))
        password = escape(request.POST.get('password'))
        print(login)
        if login == '':
            return HttpResponse('Login')
        elif password == '':
            return HttpResponse('Password')
        else:
            return HttpResponse('GOOD'+login)

    else:
        return render(request, 'mpanel/login.html')



def register(request):
    if request.method == 'POST':
        username = escape(request.POST.get('nick'))
        password = escape(request.POST.get('email'))
        print(request.POST.get('nick'))
        return HttpResponse(request.POST.get)
    else:
        return render(request,'mpanel/register.html')
