from django.urls import path
from todoapp import views

app_name = 'todo'

urlpatterns = [
    path('logout',views.userlogout , name = 'userlogout'),
    path('login',views.userlogin , name = 'userlogin'),
    path('signup',views.usersignup , name = 'usersignup'),
]
