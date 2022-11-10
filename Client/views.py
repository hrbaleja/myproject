from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.

def client(request):
    return render(request, 'Client\index.html')

def portfolio(request):
    return render(request, 'Client\Portfolio.html')

def transction(request):
    return render(request, 'Client\Transction.html')










#  Website authentication 
def u_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active and user.is_staff:
                
            if user.is_superuser :
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('office') 
            elif user.is_staff:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('client') 
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Invalid username or password.")
            return render(request, 'Client/Login.html')
    return render(request, 'Client/Login.html')


def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")

from Office.forms import Customerform, Ourserviceform, SignUpForm, Topicform


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        user = User.objects.create_user(
            username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.is_staff=True
        user.save()
        messages.info(
            request, "Account created successfully please login again")
        return redirect('login')
    else:
        form = SignUpForm()
        return render(request, 'Client/Register.html', {'form': form})   
        #return render(request, 'Client/Register.html')
       
    
