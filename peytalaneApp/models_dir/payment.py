from django.db import models
from peytalaneApp.models_dir.user import User



class Payment_option(models.Model):
    name = models.CharField(max_length=50,unique=True) 
    def __str__(self):
        return self.name


class Payment(models.Model):
    price = models.IntegerField()
    type_product = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    options = models.ManyToManyField(Payment_option,blank=True,through='Payment_option_value')
    comment = models.TextField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Payment_option_value(models.Model):
    value = models.CharField(max_length=50)
    option = models.ForeignKey(Payment_option,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
