from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BankAccountType)
admin.site.register(UserBankAccount)
admin.site.register(UserAddress)
admin.site.register(Transaction)
admin.site.register(UserIcon)
