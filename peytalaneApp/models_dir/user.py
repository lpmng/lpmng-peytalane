from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100,primary_key =True)
    lan = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    anonymous = models.BooleanField(default=False)

