from django.urls import path
from .views import anime_favorite, ListFavorites, anime_mark_movie_favorite, MovieFavoritesListView

urlpatterns = [
    path('animes/mark-fav/<int:pk>/', anime_favorite, name='mark-favorite'),
    path('anime-movies/mark-fav/<int:pk>/', anime_mark_movie_favorite, name='mark-movie-favorite'),
    path('animes/favorites/', ListFavorites.as_view(), name='favorite-animes'),
    path('anime-movies/favorites/', MovieFavoritesListView.as_view(), name='favorite-animes'),
]
