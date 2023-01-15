# DJANGO DECLARATIONS
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, Count, F, Max, Min


# DECLARING GLOBAL VARIABLES

SEX_CHOICES = [
    ("M", "M"), ("F", "F")]
IDENTITY_CHOICES = [
    ("PASSPORT", "PASSPORT"), ("ID", "ID")]
TRANSACTION_TYPES = [
    ("buy", "buy"), ("sell", "sell")]

# DECLARING CLASSES

class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile')
    username = models.CharField(
        max_length=200,
        blank=False,
        null=False)
    creation = models.DateTimeField(auto_now_add=True)
    modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    """
    Customers table. The base of the CRM
    """
    complete_name = models.CharField(
        max_length=300, null=False, blank=False)
    identity_type = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        choices=IDENTITY_CHOICES)
    identity_number = models.CharField(
        max_length=100, null=False, blank=False)
    identity_expire_date = models.DateField(null=False, blank=False)
    phone = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=300, null=True, blank=True)
    date_of_birth = models.DateField(null=False, blank=False)
    sex = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        choices=SEX_CHOICES)
    nationality = models.CharField(max_length=300, null=False, blank=False)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.complete_name

    def transactions_count(self):
        return len(Transaction.objects.filter(customer=self))

    def sell_transactions_count(self):
        return len(Transaction.objects.filter(customer=self, transaction_type="sell"))

    def buy_transactions_count(self):
        return len(Transaction.objects.filter(customer=self, transaction_type="buy"))

    def type_customer(self):
        if self.sell_transactions_count() > self.buy_transactions_count():
            return "sell"
        elif self.sell_transactions_count() > self.buy_transactions_count():
            return "buy"
        else:
            return ""

class CustomerNotes(models.Model):
    """
    Here we store all the notes and remarks about a customer
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer + str(self.created_at)


class Transaction(models.Model):
    """
    Transactions table.
    """
    transaction_type = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        choices=TRANSACTION_TYPES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    currency = models.CharField(max_length=10, null=False, blank=False)
    amount = models.FloatField()
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.transaction_type) +  " - " + str(self.customer)


class TransactionNotes(models.Model):
    """
    Here we store all the notes and remarks about a customer
    """
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer + str(self.created_at)
