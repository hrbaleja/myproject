
from django.urls import path
from Auth import views

urlpatterns = [   
    path('login', views.u_login, name='login'),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.register, name='register'),
   
]

