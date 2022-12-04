from django.db import models
from .constants import *
from django.core.validators import (MinValueValidator, MaxValueValidator,)
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class BankAccountType(models.Model):
    name = models.CharField(max_length=128)
    maximum_withdrawal_amount = models.DecimalField(decimal_places=2, max_digits=12)
    annual_interest_rate = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(
        100)], decimal_places=2, max_digits=5, help_text='Interest rate from 0 - 100')
    interest_calculation_per_year = models.PositiveSmallIntegerField(validators=[MinValueValidator(
        1), MaxValueValidator(12)], help_text='The number of times interest will be calculated per year')

    def __str__(self):
        return self.name

    def calculate_interest(self, principal):
        """
        Calculate interest for each account type. This uses a basic interest calculation formula
        """
        p = principal
        r = self.annual_interest_rate
        n = Decimal(self.interest_calculation_per_year)

        # Basic Future Value formula to calculate interest
        interest = (p * (1 + ((r/100) / n))) - p

        return round(interest, 2)


class UserBankAccount(models.Model):
    user = models.OneToOneField(
        User, related_name='account', on_delete=models.CASCADE,)
    account_type = models.ForeignKey(
        BankAccountType, related_name='accounts', on_delete=models.CASCADE)
    account_no = models.PositiveIntegerField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    birth_date = models.DateField(null=True, blank=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    interest_start_date = models.DateField(null=True, blank=True, help_text=(
        'The month number that interest calculation will start from'))
    initial_deposit_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.account_no)

    def get_interest_calculation_months(self):
        """
        List of month numbers for which the interest will be calculated

        returns [2, 4, 6, 8, 10, 12] for every 2 months interval
        """
        interval = int(12 / self.account_type.interest_calculation_per_year)
        start = self.interest_start_date.month
        return [i for i in range(start, 13, interval)]


class UserAddress(models.Model):
    user = models.OneToOneField(
        User, related_name='address', on_delete=models.CASCADE,)
    street_address = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length=256,choices=COUNTRY_CHOICES)

    def __str__(self):
        return self.user.email


class Transaction(models.Model):
    account = models.ForeignKey(
        UserBankAccount, related_name='transactions', on_delete=models.CASCADE,)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.CharField(max_length=256,  choices=TRANSACTION_TYPE)
    referenceno = models.DecimalField(decimal_places=0, max_digits=12)
    balance_after_transaction = models.DecimalField(
        decimal_places=2, max_digits=12)
    transaction_type = models.CharField(max_length=100,
        choices=TRANSACTION_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account.account_no)

    class Meta:
        ordering = ['timestamp']


class UserIcon(models.Model):
    user = models.OneToOneField(User, related_name='UserIcon', on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='Database Image/UserIcon', blank=True)
