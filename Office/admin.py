from django.contrib import admin
from Office.models import *

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'image','people','discount','price','lista','listb','listc','listd','liste')
admin.site.register(Ourservice,ServiceAdmin)

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id','Title', 'image','Category','Group','Time')
admin.site.register(OurArea,AreaAdmin)

class ContactuAdmin(admin.ModelAdmin):
    list_display = ('id','Topic', 'First_Name','Last_Name','Email','Contact','Message')
admin.site.register(Contactu,ContactuAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','First_name', 'Last_name','Address','DOB','Email','Contact')
admin.site.register(Customer,CustomerAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id','Title')
admin.site.register(Topic,TopicAdmin)
class messageAdmin(admin.ModelAdmin):
    list_display = ('id','Image', 'Company','Desc','Icon','Person','Designation')
admin.site.register(About,messageAdmin)
