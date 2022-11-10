from django.shortcuts import render,redirect
from django.contrib import messages
from Office.models import Topic, Ourservice,OurArea,Contactu
from Office.forms import Ourserviceform
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
    return render(request, "Home\About.html")


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

def info(request):
    prg = Ourservice.objects.all()   
    return render(request, "Info.html",{'Ourservice': prg})


def data(request):   
    if request.method == "POST":
        form = Ourserviceform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('service')
            except:
                pass
    else:
        form = Ourserviceform()
    return render(request, 'data.html', {'form': form})
    