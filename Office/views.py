from django.contrib import messages
from django.shortcuts import render,redirect
from Office.models import  Ourservice,OurArea,Contactu,Customer,Topic
from django.contrib.auth import  logout
from Office.forms import Ourserviceform

# Create your views here.
def index(request):
    return render(request, 'Home\index.html')
    
def office(request):   
    Contacts=Contactu.objects.all().count()
    Customers = Customer.objects.all().count()
    Areao = OurArea.objects.all().count()       
    Services = Ourservice.objects.all().count() 
    Topics = Topic.objects.all().count()
    context ={'messagesum':Contacts,'customersum': Customers,'areasum':Areao,'servicesum':Services,'valuesum':Topics}
    return render(request, "Office\index.html", context )
    

def clientoffice(request):      
    Contacts=Contactu.objects.all()
    Customers = Customer.objects.all() 
    context ={'Contactus':Contacts,'Customer': Customers}
    return render(request, "Office\Client.html", context )
    

def recordoffice(request):   
    Topics = Topic.objects.all() 
    Areao = OurArea.objects.all()       
    Services = Ourservice.objects.all()          
    context ={'Topic': Topics,'ourservice': Services,'ourArea': Areao}
    return render(request, "Office\Record.html", context )

def Aservice(request):   
    if request.method == "POST":
        form = Ourserviceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recordoffice')           
    else:
        form = Ourserviceform()
    return render(request, 'Office\Service.html', {'form': form})

def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")