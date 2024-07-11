from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import AnimeViewSet, AnimeMovieViewSet


router = DefaultRouter()

router.register(r'', AnimeViewSet, basename='animes')
router.register(r'movie', AnimeMovieViewSet, basename='anime-movies')


urlpatterns = router.urls