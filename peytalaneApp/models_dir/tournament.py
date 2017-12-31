from django.db import models
from peytalaneApp.models_dir.user import User

class Tournament(models.Model):
    nom = models.CharField(max_length=50)
    participants = models.ManyToManyField(User)
    number_participants = models.IntegerField()
    