from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # portfolio and picture

    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True)

    