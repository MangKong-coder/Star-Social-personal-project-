from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    bday = models.DateField()
    def __str__(self):
        return self.name


class User(models.Model):
    usr = models.IntegerField(unique=True)
    def __str__(self):
        return str(self.usr)

class Webpage(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)