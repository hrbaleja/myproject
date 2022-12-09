from Office.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import *


def u_login(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active and user.is_staff:
                if user.is_superuser:
                    login(request, user)
                    messages.info(
                        request, f"You are now logged in as {username}.")
                    return redirect('office')
                elif user.is_staff:
                    login(request, user)
                    messages.info(
                        request, f"You are now logged in as {username}.")
                    return redirect('client')
            else:
                # Return an 'invalid login' error message.
                messages.error(request, "Invalid username or password.")
                return render(request, 'Auth/Login.html')
        return render(request, 'Auth/Login.html')
    else:
        messages.success(request, "You are Already Logged in!!")
        return redirect("index")


def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Account created successfully please login again")
            return redirect('login')           
    else:
        form = SignUpForm()        
        return render(request, 'Auth/Register.html', {'form': form})
        # return render(request, 'Client/Register.html')
