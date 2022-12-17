from rest_framework import serializers
from MovieApp.admin import *
class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name')

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'movie')

class MoviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title', 'description', 'duration', 'director')
