from django.urls import path
from Client import views

urlpatterns = [
    path('', views.client, name='client'),
    path('login', views.u_login, name='login'),
    path('logout', views.logoutUser,name="logout"),
    path('register',views.register, name = 'register') ,
    
    path('portfolio', views.portfolio,name="portfolio"),
    path('transction',views.transction, name = 'transction') ,
]
