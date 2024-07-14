from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import AnimeViewSet, AnimeMovieViewSet, AnimeCharacterViewSet


router = DefaultRouter()

router.register(r'animes', AnimeViewSet, basename='animes')
router.register(r'movie', AnimeMovieViewSet, basename='anime-movies')
router.register(r'character', AnimeCharacterViewSet, basename='character')


urlpatterns = router.urls