from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status


from .serializers import AnimeMovieSerializer, AnimeSerializer
from base.views import BaseViewSet
from animes.models import Anime, AnimeMovie

class AnimeViewSet(BaseViewSet):
    serializer_class = AnimeSerializer

class AnimeMovieViewSet(BaseViewSet):
    serializer_class = AnimeMovieSerializer


@api_view(['PUT', 'GET'])
def anime_mark_movie_favorite(request, pk=None):
    if request.method == 'PUT':

        anime_movie = AnimeMovie.objects.get(id=pk, is_active= True)

        if anime_movie:
            anime_movie.is_favorite = not anime_movie.is_favorite
            anime_movie.save()
            return Response({"message":f"Anime marcado como {'Favorito' if anime_movie.is_favorite else 'No favorito'}"}, status=status.HTTP_200_OK)
        return Response({"error": "No se encontro el anime"}, status=status.HTTP_400_BAD_REQUEST)



class MovieFavoritesListView(generics.ListAPIView):
    serializer_class = AnimeMovieSerializer
    queryset = AnimeMovie.objects.filter(is_active = True, is_favorite = True)


@api_view(['PUT', 'GET'])
def anime_favorite(request, pk=None):
    if request.method == 'PUT':

        anime = AnimeSerializer.Meta.model.objects.get(id=pk, is_active= True)

        if anime:
            anime.is_favorite = not anime.is_favorite
            anime.save()
            return Response({"message":f"Anime marcado como {'Favorito' if anime.is_favorite else 'No favorito'}"}, status=status.HTTP_200_OK)
        return Response({"error": "No se encontro el anime"}, status=status.HTTP_400_BAD_REQUEST)


class ListFavorites(generics.ListAPIView):
    serializer_class =AnimeSerializer
    queryset = Anime.objects.filter(is_active = True, is_favorite = True)

