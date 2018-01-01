from django.db import models

class Payment(models.Model):
    price = models.IntegerField()
    product = models.CharField(max_length=100)