from django.contrib import admin

# Register your models here.
from .models import Anime, AnimeMovie

admin.site.register(Anime)
admin.site.register(AnimeMovie)