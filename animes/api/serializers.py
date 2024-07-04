from rest_framework import serializers

from animes.models import Anime, AnimeMovie
from base.models import Category



class CategorySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Category
        fields = '__all__'

class AnimeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Anime
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'name': instance.name,
            'rating': instance.rating,
            'category': instance.category.name,
            'chapters': instance.chapters,
            'seasons': instance.seasons,
            'image': instance.image.url,
            'sinopsis': instance.sinopsis,
        }

class AnimeMovieSerializer(serializers.ModelSerializer):


    class Meta:
        model = AnimeMovie
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'name': instance.name,
            'rating': instance.rating,
            'category': instance.category.name,
            'duration': instance.duration,
            'image': instance.image.url,
            'sinopsis': instance.sinopsis,
        }