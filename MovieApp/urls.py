from django.urls import path
from MovieApp.views import *

urlpatterns = [
    path('Directors/', Director_view),
    path('Directors/<int:id>/', Director_view_detail),
    path('Reviews/', Review_view),
    path('Reviesw/<int:id>/', Review_view_detail),
    path('Movies/', Movie_view),
    path('Movies/<int:id>/', Movie_view_detail),
]
