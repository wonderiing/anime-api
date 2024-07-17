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
    
class AnimeCharacter(models.Model):
    name = models.CharField(max_length=155, null=False,blank=False)
    age = models.IntegerField(null=False,blank=False)
    info = models.TextField(null=False,blank=False)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, null=True, blank=True, related_name='anime_characters')
    anime_movie = models.ForeignKey(AnimeMovie, on_delete=models.CASCADE,  null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_favorite = models.BooleanField(default=False)
    image = models.ImageField(upload_to='anime_images/', null=True, blank=True)


    class Meta:
        verbose_name = 'Personaje'
        verbose_name_plural = 'Personajes'


    def __str__(self):
        return 'Character #{}'.format(self.id)