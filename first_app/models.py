from django.db import models

#Create your models here.

class Songs(models.Model):
    song_name=models.CharField(max_length=1000)
    choice=(
      ('Hindi','Hindi'),
      ('English','English'),
      ('Punjabi','Punjabi'),
      )
    category=models.CharField(max_length=100,choices=choice)
    img=models.ImageField(upload_to='pics')
    audio_file =models.CharField(max_length=1000)
    album=models.CharField(max_length=100)
    artist=models.CharField(max_length=500)
    
    def __str__(self):
      return self.song_name