from django.urls import path
from Home import views

urlpatterns = [
   path('', views.index, name='index'),
   path('service', views.Service, name='Service'),
   path('area', views.Area, name='Area'),
   path('about', views.About, name='About'),
   path('contact', views.Contact, name='Contact'),
   path('Brochure', views.Brochure,name='Brochure'), 
  
]



