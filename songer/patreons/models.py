from django.db import models

# Create your models here.
class Patreon(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    review = models.CharField(max_length=2000)
    pat_id = models.ForeignKey(Patreon,on_delete=models.CASCADE)
    claps = models.IntegerField()

