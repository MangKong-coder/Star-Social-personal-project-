from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=50,)
    lname = models.CharField(max_length=50,)
    email = models.EmailField(max_length=160, unique=True)

    