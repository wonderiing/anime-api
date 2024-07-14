from django.contrib import admin

# Register your models here.
from .models import Anime, AnimeMovie, AnimeCharacter

admin.site.register(Anime)
admin.site.register(AnimeMovie)
admin.site.register(AnimeCharacter)