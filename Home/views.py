from django.shortcuts import render,redirect
from django.contrib import messages
from Office.models import *
from Office.forms import Ourserviceform
from Office.models import About
# Create your views here.
def index(request):
    return render(request, 'Home\index.html')


def Service(request):
    prg = Ourservice.objects.all()   
    return render(request, "Home\Service.html",{'Ourservice': prg})
    

def Area(request):
    Areao = OurArea.objects.all()   
    return render(request, "Home\Area.html",{'OurArea': Areao})
    

def About(request):
  #  Abou= About.objects.all()    
   # context ={'About':Abou}
    return render(request, "Home\About.html" )
 


def Contact(request):
        if request.method == 'POST':
                First_Name = request.POST['First_Name']
                Last_Name = request.POST['Last_Name']
                Email = request.POST['Email']
                Contact = request.POST['Contact']
                Message = request.POST['Message']           
                Query = Contactu.objects.create(
                First_Name=First_Name, Last_Name=Last_Name, Email=Email, Contact=Contact,Message=Message)
                Query.save()
                messages.info(request, "Thank you for getting in touch !  ")
                return redirect('Contact')
        else:
            Topi = Topic.objects.all()   
            return render(request, "Home\Contact.html",{'Topic': Topi})  



# report mate no code
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import  A4
from reportlab.lib.units import inch


def Brochure(request):    
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)    
    p.translate(inch,inch)
    # define a large font
    p.setFont("Helvetica", 14)    
    my_image = ImageReader('Static/Images/favicon.png')
    p.drawImage(my_image, 10, 600, mask='auto')
    ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')  
    p.drawString( 0,700,ts )
    p.drawString(100, 100,"Hello World")
    p.setTitle('Brochure')
    p.showPage() 
    p.save() 
    buffer.seek(0)   
    return FileResponse(buffer, as_attachment=True, filename="Brochure.pdf")



    
    """
    if request.user.is_anonymous: 
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("data")
            else:
                messages.error(request, "Invalid username or password.")
                return render(request, 'Client/Login.html')
        return render(request, 'Auth/Login.html')        
        
    else:
        return redirect("data")
    """