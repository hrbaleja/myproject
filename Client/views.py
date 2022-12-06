import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def client(request):
    return render(request, 'Client\index.html')

def portfolio(request):
    return render(request, 'Client\Portfolio.html')

def transction(request):
    return render(request, 'Client\Transction.html')



def account(request):
    date = datetime.datetime.now().strftime(" %d-%m-%Y")    
    acc = UserBankAccount.objects.filter(user = request.user)   
    tr= Transaction.objects.filter(account=request.user.account)
    add=UserAddress.objects.filter(user=request.user)
    icon=UserIcon.objects.filter(user=request.user)
    context = {'date': date,'UserBankAccount': acc,'Transaction':tr,'UserAddress':add,'UserIcon':icon}
    return render(request, "Client\Account.html", context)
