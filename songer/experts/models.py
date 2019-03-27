from django.db import models

# Create your models here.

class experts(models.Model):

    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.username

class ExpertReview(models.Model):
    expert_review_id = models.IntegerField(primary_key=True)
    review = models.CharField(max_length=2000)
    #pat_id = models.ForeignKey(experts,on_delete=models.CASCADE)
    expert_album_id = models.ForeignKey('songer_admn.Album',on_delete=models.CASCADE,default=None)
    claps = models.IntegerField(default=0)

    def __str__(self):
        return self.review
