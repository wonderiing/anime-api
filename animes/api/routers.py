from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import AnimeViewSet, AnimeMovieViewSet


router = DefaultRouter()

router.register(r'animes', AnimeViewSet, basename='animes')
router.register(r'anime-movies', AnimeMovieViewSet, basename='anime-movies')

urlpatterns = router.urls