from django.db import models

#Create your models here.
class Album(models.Model):
  album_title=models.CharField(max_length=255)
  img=models.ImageField(upload_to='pics')
  choice=(
      ('Hindi','Hindi'),
      ('English','English'),
      ('Punjabi','Punjabi'),
      )
  category=models.CharField(max_length=100,choices=choice)

  def __str__(self):
    return self.album_title

class Song(models.Model):
    song_name=models.CharField(max_length=1000)
    song_url=models.CharField(max_length=1000)
    album_id=models.ForeignKey(Album,default=None,on_delete=models.CASCADE)
    song_artist=models.CharField(max_length=500)
    
    def __str__(self):
      return self.song_name

  

class playlist(models.Model):
  playlist_title=models.CharField(max_length=255)
  playlist_curator=models.CharField(max_length=255)
  playlist_art=models.ImageField(upload_to='pics')

class song_to_playlist(models.Model):
  song_id=models.IntegerField()
  playlist_id=models.IntegerField()