from django.db import models


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

    class Meta:  
        db_table = "Customer" 
    def __str__(self):
        return self.First_name

class Topic(models.Model):  
    Title = models.CharField(max_length=100)     
    
    def __str__(self):
        return self.Title
