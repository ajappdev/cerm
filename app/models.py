# DJANGO DECLARATIONS
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, Count, F, Max, Min


# DECLARING GLOBAL VARIABLES
SEX_CHOICES = [
    ("M", "M"), ("F", "F")]
IDENTITY_CHOICES = [
    ("PASSPORT", "PASSPORT"), ("ID", "ID")]
    
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
    phone = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField()
    sex = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        choices=SEX_CHOICES)
    nationality = models.CharField(max_length=300, null=False, blank=False)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomerNotes(models.Model):
    """
    Here we store all the notes and remarks about a customer
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)