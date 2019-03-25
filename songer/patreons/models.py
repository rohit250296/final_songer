
from django.db import models
from django.apps import apps

# Create your models here.
#Album = apps.get_model('patreons','Album')
class Patreon(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    review = models.CharField(max_length=2000)
    pat_id = models.ForeignKey(Patreon,on_delete=models.CASCADE)
    album_id = models.ForeignKey('songer_admn.Album',on_delete=models.CASCADE,default=None)
    claps = models.IntegerField(default=0)

    def __str__(self):
        return self.review
