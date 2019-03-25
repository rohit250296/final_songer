from django.db import models

# Create your models here.
class Band(models.Model):
    band_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    formed = models.CharField(max_length=30)
    image_url = models.CharField(max_length=40)
    website_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BandMember(models.Model):
    member_id = models.IntegerField(primary_key=True)
    member_name = models.CharField(max_length=100,null=False,default=None)
    band_id = models.ForeignKey(Band,on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=40)
    def __str__(self):
        return self.member_name

class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    genre_name = models.CharField(max_length=40)
    def __str__(self):
        return self.genre_name

class Album(models.Model):
    album_id = models.IntegerField(primary_key=True)
    released_on = models.DateField()
    label = models.CharField(max_length=40)
    genre_id = models.ForeignKey(Genre,on_delete=models.CASCADE)
    band_id = models.ForeignKey(Band,on_delete=models.CASCADE)
    cover_url = models.CharField(max_length=200)
    def __str__(self):
        return self.label


class Song(models.Model):
    song_id = models.IntegerField(primary_key=True)
    song_name = models.CharField(max_length=200)
    album_id = models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):
        return self.song_name

class News(models.Model):
    news_id = models.IntegerField(primary_key=True)
    headline = models.CharField(max_length=200,null=False,default=None)
    news_desc = models.CharField(max_length=1000)
    cover_url = models.CharField(max_length=100)
    def __str__(self):
        return self.headline

class Single(models.Model):
    single_id = models.IntegerField(primary_key=True)
    single_name = models.CharField(max_length=200)
    cover_url = models.CharField(max_length=200)
    singer = models.CharField(max_length=30)
    album_id = models.ForeignKey(Album,on_delete=models.CASCADE)
    def __str__(self):
        return self.single_name




