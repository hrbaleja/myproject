from django.contrib import messages
from django.shortcuts import render,redirect
from Office.models import *
from django.contrib.auth import  logout
from Office.forms import Ourserviceform
from django.contrib.auth.decorators import user_passes_test
from .fusioncharts import FusionCharts
from django.db.models import Sum


# Create your views here.
import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
def index(request):
    return render(request, 'Home\index.html')

@user_passes_test(lambda u: u.is_superuser,login_url='login')
def office(request): 
    dataSource = {}
    dataSource['chart'] = {
        "caption": "Manage analytics like a boss",
            "subCaption" : "For a net-worth of $1M",
            "showValues":"1",
            "showPercentInTooltip" : "1",
            "numberPrefix" : "₹",
            "enableMultiSlicing":"1",
            "theme": "fusion",
            "exportEnabled": "1",         
           # "exportFormats": "JPG=Export as High Quality Image|PNG=Export as High Quality Image|PDF=Export as Printable|XLSX=Export Chart Data|CSV=Export Chart CSV",
           # "exportTargetWindow": "_self",
            "exportFileName": "Monthly_Revenue",            
        }   
    dataSource['data'] = []
    for key in Revenue.objects.all():
      data = {}
      data['label'] = key.Month
      d = Decimal(key.Revenue)     
      data['value'] =  json.dumps(d, cls=DecimalEncoder)
      dataSource['data'].append(data)
    
    dataSourcea = {}
    dataSourcea['chart'] = {
        "caption": "Manage analytics like a boss",
            "subCaption" : "For a net-worth of $1M",
            "showValues":"1",
            "showPercentInTooltip" : "1",
            "numberPrefix" : "₹",
            "numbersuffix": "M",
            "enableMultiSlicing":"1",
            "theme": "gammel",
            "exportEnabled": "1",  
            "xaxisname": "Month",
            "yaxisname": "Monthy Revenue",       
           # "exportFormats": "JPG=Export as High Quality Image|PNG=Export as High Quality Image|PDF=Export as Printable|XLSX=Export Chart Data|CSV=Export Chart CSV",
           # "exportTargetWindow": "_self",
            "exportFileName": "Monthly_Revenue",            
        }   
    dataSourcea['data'] = []
    for key in Revenue.objects.all():
      data = {}
      data['label'] = key.Month
      d = Decimal(key.Revenue)     
      data['value'] =  json.dumps(d, cls=DecimalEncoder)
      dataSourcea['data'].append(data)
      
    # Create an object for the overlappedbar2d chart using the FusionCharts class constructor
    overlappedcolumn2d = FusionCharts("column3d", "ex1" , "1000", "400", "chart-1", "json", dataSourcea)

       
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("pie3d", "ex2" , "100%", "500", "chart-2", "json", dataSource)   
    
   # context={'output1' : overlappedcolumn2d.render(), 'output2' : column2d.render()}
    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 

    Contacts=Contactu.objects.all().count()
    Customers = Customer.objects.all().count()
    Areao = OurArea.objects.all().count()       
    Services = Ourservice.objects.all().count() 
    Topics = Topic.objects.all().count()
    Revenues= Revenue.objects.all().aggregate(Sum('Revenue'))['Revenue__sum'] or 0.00
    context ={'messagesum':Contacts,'customersum': Customers,'areasum':Areao,
    'servicesum':Services,'valuesum':Topics,'Revenu':Revenues,'output1' : overlappedcolumn2d.render(),
     'output2' : column2d.render()}
    return render(request, "Office\index.html", context )
    
@user_passes_test(lambda u: u.is_superuser,login_url='login')
def clientoffice(request):      
    Contacts=Contactu.objects.all()
    Customers = Customer.objects.all() 
    context ={'Contactus':Contacts,'Customer': Customers}
    return render(request, "Office\Client.html", context )
    
@user_passes_test(lambda u: u.is_superuser,login_url='login',)
def recordoffice(request):   
    Topics = Topic.objects.all() 
    Areao = OurArea.objects.all()       
    Services = Ourservice.objects.all()          
    context ={'Topic': Topics,'ourservice': Services,'ourArea': Areao}
    return render(request, "Office\Record.html", context )

@user_passes_test(lambda u: u.is_superuser,login_url='login')
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