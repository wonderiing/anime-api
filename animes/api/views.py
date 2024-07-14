from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes, action
from rest_framework.response import Response
from rest_framework import status


from .serializers import AnimeMovieSerializer, AnimeSerializer, AnimeCharacterSerializer
from base.views import BaseViewSet
from animes.models import Anime, AnimeMovie


class AnimeViewSet(BaseViewSet):
    serializer_class = AnimeSerializer

    @action(detail=True, methods=['put'], url_path='mark-fav')
    def mark_favorite(self,request,pk=None):
        
        anime = Anime.objects.get(id=pk, is_active=True)

        if anime:
            anime.is_favorite = not anime.is_favorite
            boolean = anime.is_favorite
            anime.save()
            return Response({"message": f"Anime marcado como {'Favorito' if boolean else 'No favorito'}"})
        return Response({"error": "Ese anime no se encontro"})
        

    @action(detail=False, methods=['get'], url_path='favorites')
    def list_favorites(self,request):
        
        animes = Anime.objects.filter(is_active = True, is_favorite= True)

        serializer = AnimeSerializer(animes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AnimeMovieViewSet(BaseViewSet):
    serializer_class = AnimeMovieSerializer

    @action(detail=True, methods=['put'], url_path='movie-mark-fak')
    def mark_favorite(self,request,pk=None):

        anime = AnimeMovie.objects.get(is_active=True, id=pk)

        if anime:
            anime.is_favorite = not anime.is_favorite
            boolean = anime.is_favorite
            anime.save()
            return Response({"message": f"Pelicula marcada como {'Favorito' if boolean else 'No Favorito'} "}, status=status.HTTP_200_OK)
        return Response({"error": "anime not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'], url_path='favorite-movies')
    def list_favorite(self,request,pk=None):

        favorite_movies = AnimeMovie.objects.filter(is_active=True, is_favorite=True)

        serializer = AnimeMovieSerializer(favorite_movies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AnimeCharacterViewSet(BaseViewSet):
    serializer_class = AnimeCharacterSerializer








