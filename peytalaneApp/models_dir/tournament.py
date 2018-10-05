from django.db import models
from peytalaneApp.models_dir.user import User

class Participant(models.Model):
    game_pseudo = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " dit " + self.game_pseudo

class Tournament(models.Model):
    name = models.CharField(max_length=50)
    participants = models.ManyToManyField(Participant,null=True,blank=True)
    number_participants = models.IntegerField()
    img = models.FileField(upload_to='peytalaneApp/static/')
    price = models.IntegerField()

    @property
    def img_src(self):
        return self.img.url.replace("peytalaneApp","")
