from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RecommendationView(APIView):
    def get(self, request):
        data = {"message": "hello i am music api"}  # Response data
        return Response(data, status=status.HTTP_200_OK)  # Returning response
