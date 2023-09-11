from django.db import models
from django.contrib.auth.models import AbstractUser

ACCOUNT_TYPE = [('student', 'Student'), ('teacher', 'Teacher')]

class CustomUser(AbstractUser):
    account_type = models.CharField(max_length=7, choices=ACCOUNT_TYPE)
    display_name = models.CharField(Max_length=20)