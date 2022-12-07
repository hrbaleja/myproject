from django.db import models
from django.db import models
from Client.constants import *
from django.contrib.auth.models import User

class Ourservice(models.Model):
    image=models.ImageField(upload_to='Dataimage', blank=True)
    title=models.CharField(max_length=100)
    people=models.CharField(max_length=10)
    discount=models.CharField(max_length=10)
    price=models.CharField( max_length=10)
    lista=models.CharField(max_length=100)
    listb=models.CharField(max_length=100)
    listc=models.CharField(max_length=100)
    listd=models.CharField(max_length=100,blank=True)
    liste=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.title

class OurArea(models.Model):
    image=models.ImageField(upload_to='Areaimage')
    Title=models.CharField(max_length=100)
    Category=models.CharField(max_length=50)
    Group=models.CharField(max_length=50)
    Time=models.CharField( max_length=10)
    Desc=models.CharField(max_length=500)
  

    def __str__(self):
        return self.Title

class Contactu(models.Model):
    Topic=models.CharField(max_length=50,blank=True)
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.CharField(max_length=10)
    Message=models.CharField(max_length=500)

    def __str__(self):
        return self.First_Name


class Customer(models.Model):  
    First_name = models.CharField(max_length=100)  
    Last_name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)  
    DOB = models.DateField()
    Email = models.EmailField()
    password = models.CharField(max_length=50)  
    Contact = models.CharField(max_length=10) 


    def __str__(self):
        return self.First_name

class Topic(models.Model):  
    Title = models.CharField(max_length=100)     
    
    def __str__(self):
        return self.Title

class About(models.Model):
    Image=models.ImageField(upload_to='Aboutcompany')
    Company=models.CharField(max_length=256,  choices=COMPANY_CHOICES)
    Desc=models.CharField(max_length=500)
    Icon=models.ImageField(upload_to='Abouticon')
    Person=models.OneToOneField(  User,  on_delete=models.CASCADE,)
    Designation=models.CharField(max_length=100) 
    Time = models.DateTimeField(auto_now_add=True)

  

    def __str__(self):
        return self.Company
class Revenue(models.Model):
    Revenue = models.DecimalField(decimal_places=2, max_digits=12)
    Month = models.CharField(max_length=256,  choices=Month_Choice)

    def __str__(self):
        return str(self.Month)