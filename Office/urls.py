from django.urls import path
from Office import views

urlpatterns = [
   
   path('', views.office,name="office"),
   path('clientoffice', views.clientoffice,name="clientoffice"),
   path('recordoffice', views.recordoffice,name="recordoffice"),
   path('logout', views.logoutUser,name="logout"),
   path('Service',views.Service,name="Service"),
  
]
