from django.db import models
from django.contrib.auth.models import User

ACCOUNT_TYPE = [('student', 'Student'), ('teacher', 'Teacher')]

class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=7, choices=ACCOUNT_TYPE)
    display_name = models.CharField(max_length=20)