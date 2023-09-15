from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ACCOUNT_TYPE = [('student', 'Student'), ('teacher', 'Teacher')]

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=7, choices=ACCOUNT_TYPE, default='student')
    display_name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.display_name} @{self.user.username}"
    
    class Meta:
        verbose_name_plural = "Custom Users"
    
    def save(self, *args, **kwargs):
        if not self.display_name:
            self.display_name = self.user.username
        super().save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_or_update_user(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)
        instance.customuser.save()