from django.db import models

# Create your models here.
from base.models import BaseModel

class Anime(BaseModel):
    seasons = models.IntegerField(null=False,blank=False)
    chapters = models.IntegerField(null=False,blank=False)
    sinopsis = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'


    def __str__(self):
        return self.name

class AnimeMovie(BaseModel):
    duration = models.CharField(max_length=15, null=False,blank=False)
    sinopsis = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = 'Anime Pelicula'
        verbose_name_plural = 'Anime Peliculas'


    def __str__(self):
        return self.name