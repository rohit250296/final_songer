from django.db import models

# Create your models here.
class Band(models.Model):
    band_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    formed = models.CharField(max_length=30)
    image_url = models.CharField(max_length=40)
    website_url = models.CharField(max_length=200)


class BandMember(models.Model):
    member_id = models.IntegerField(primary_key=True)
    band_id = models.ForeignKey(Band,on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=40)

class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    genre_name = models.CharField(max_length=40)

class Album(models.Model):
    album_id = models.IntegerField(primary_key=True)
    released_on = models.DateField()
    label = models.CharField(max_length=40)
    genre_id = models.ForeignKey(Genre,on_delete=models.CASCADE)
    cover_url = models.CharField(max_length=200)


class Song(models.Model):
    song_id = models.IntegerField(primary_key=True)
    song_name = models.CharField(max_length=200)
    album_id = models.ForeignKey(Album,on_delete=models.CASCADE)

class News(models.Model):
    news_id = models.IntegerField(primary_key=True)
    news_desc = models.CharField(max_length=1000)
    cover_url = models.CharField(max_length=100)

class Single(models.Model):
    single_id = models.IntegerField(primary_key=True)
    single_name = models.CharField(max_length=200)
    cover_url = models.CharField(max_length=200)
    singer = models.CharField(max_length=30)
    album_id = models.ForeignKey(Album,on_delete=models.CASCADE)



