from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=20)




