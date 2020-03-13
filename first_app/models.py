from django.db import models

#Create your models here.

class Songs(models.Model):
    song_name=models.CharField(max_length=1000)
    choice=(
      ('Hindi','H'),
      ('English','E'),
      ('Punjabi','P'),
      )
    category=models.CharField(max_length=100,choices=choice)
    img=models.ImageField(upload_to='pics')
    audio_file =models.FileField(upload_to='audiofile')
    album=models.CharField(max_length=100)
    artist=models.CharField(max_length=500)
    
    def __str__(self):
      return self.song_name