from django.shortcuts import render, redirect
from django.contrib import auth
from accounts.models import User
import datetime


def home(request):
    if request.user.is_authenticated == False and request.method == 'POST':
        random_username = datetime.datetime.today().strftime("%m-%d %H:%M:%S.%f")
        print(random_username)
        new_user = User.objects.create(
            username=random_username,
            email='',
            password='verydifficultpassword',
        )
        auth.login(request, new_user)
        return redirect('lecture/')
    return render(request, 'homepage.html')
