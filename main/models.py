from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.models import User


class Petition(models.Model):
    def __str__(self):
        return self.title
    image = models.ImageField(upload_to='main')
    title = models.CharField(max_length=60, null=True)
    text = models.TextField(null=True)
    date = models.DateField(default=now())
    votes = models.IntegerField(default=0)
    finish = models.BooleanField(default=False)


class Citizen(models.Model):
    def __str__(self):
        return self.user.first_name + self.user.last_name
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pin = models.CharField(max_length=14, unique=True)
    phone = models.CharField(max_length=12, unique=True)
    pets = models.ManyToManyField(Petition)
