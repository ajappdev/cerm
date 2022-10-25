# DJANGO DECLARATIONS
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, Count, F, Max, Min


# DECLARING GLOBAL VARIABLES


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

