from django.urls import path
from .views import RecommendationView,MusicRecommenderAI

urlpatterns = [
    path('music/', RecommendationView.as_view(), name='music-api'),
    path('recommend',MusicRecommenderAI.as_view(), name='music-recommender')
]