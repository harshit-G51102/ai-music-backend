from django.urls import path
from .views import RecommendationView

urlpatterns = [
    path('music/', RecommendationView.as_view(), name='music-api'),
]