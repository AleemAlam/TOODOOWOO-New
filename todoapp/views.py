from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def index(request):
    return render(request,'todoapp/index.html')


def usersignup(request):
    if request.method == 'POST':
        if request.POST['password1']== request.POST['password2']:
            try:
                user =  User.objects.create_user(username = request.POST['username'],password = request.POST['password1'])
                user.save()
                login(request,user)
                return render(request,'todoapp/index.html',{'user':user})
            except IntegrityError:
                return render(request, 'todoapp/usersignup.html',{'form': UserCreationForm(),'error': 'Username alredy registered'})
        else:
            return render(request, 'todoapp/usersignup.html',{'form': UserCreationForm(),'error': 'Password has to be mached'})

    else:
        return render(request, 'todoapp/usersignup.html',{'form': UserCreationForm()})

def userlogout(request):
    logout(request)
    return redirect('index')


def userlogin(request):
    if request.method == 'POST':
        user =  authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'todoapp/userlogin.html',{'form': AuthenticationForm(),'error': 'Username and password did not matched'})
        else:
            login(request,user)
            return render(request,'todoapp/index.html',{'user':user})
    else:
        return render(request, 'todoapp/userlogin.html',{'form': AuthenticationForm()})
