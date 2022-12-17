from django.shortcuts import render
from django.urls import path
from MovieApp.urls import *
from MovieApp.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from MovieApp.serializers import *
from rest_framework import status


@api_view(['GET'])
def Director_view(request):
    if request.method == 'GET':
        Directors = Director.objects.all()
        serializers = DirectorSerializers(Directors, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def Director_view_detail(request, **kwargs):
    if request.method == 'GET':
        Directors = Director.objects.all()
        serializers = DirectorSerializers(Directors, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def Movie_view(request):
    if request.method == 'GET':
        Movies = Movie.objects.all()
        serializers = MoviewSerializers(Movies, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def Movie_view_detail(request, **kwargs):
    if request.method == 'GET':
        Movies = Movie.objects.all()
        serializers = MoviewSerializers(Movies, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def Review_view(request):
    if request.method == 'GET':
        Reviews = Review.objects.all()
        serializers = ReviewSerializers(Reviews, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def Review_view_detail(request, **kwargs):
    if request.method == 'GET':
        Reviews = Review.objects.all()
        serializers = ReviewSerializers(Reviews, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
