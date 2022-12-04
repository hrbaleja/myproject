
from django.urls import path
from Client import views

urlpatterns = [
    path('', views.client, name='client'), 
    path('account', views.account, name='account'),
    path('portfolio', views.portfolio, name="portfolio"),
    path('transction', views.transction, name='transction'),
   
]

