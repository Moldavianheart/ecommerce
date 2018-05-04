from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.html import escape
from Mpanel.forms import RegForm


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
        form = RegForm(request.POST)
        if  form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            form = RegForm()
            return redirect('/')

        # username = escape(request.POST.get('nick'))
        # email = escape(request.POST.get('email'))
        # password = escape(request.POST.get('password'))
        # password2 = escape(request.POST.get('password'))
        args = {'form':form,'text':text}
        return
        #return HttpResponse(request.POST.get('email'))
    else:
        form = RegForm
        return render(request,'mpanel/register.html',{'form':form})
