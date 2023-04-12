from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='static/images/profile_pics/',blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    GENDER_CHOICES = (
        ('M', '男性'),
        ('F', '女性'),
    )
    address = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    birth_date = models.DateField(blank=True,null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user_id
