from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google import genai
import json

class RecommendationView(APIView):
    def get(self, request):
        data = {"message": "hello i am music api"}  # Response data
        return Response(data, status=status.HTTP_200_OK)  # Returning response


class MusicRecommenderAI(APIView):
    def post(self, request):
        # Initialize the genai client with the API key from settings
        client = genai.Client(api_key='AIzaSyCNnQ09gIwsFrtVpcL-hol_f7b7_WwoVyQ')
        
        # Get user query (you can also use `request.data.get('query', '')` if provided from the frontend)
        user_query = request.data.get('query', '')
        
        # Generate the music recommendation content

        instructions = """
            You are a music recommendation assistant. Based on the user query, your task is to recommend 5 songs that fit the query's mood, genre, or theme. For each song, generate a JSON object containing the following keys:
            name: Title of the song.
            artist: The main artist or band performing the song.
            album: The album the song belongs to.
            release_date: The song's release date in YYYY-MM-DD format.
            themes: A list of themes or moods the song conveys (e.g., love, nostalgia, empowerment, sadness).
            album_art: URL to the album cover image.
            You_tube_link: You Tube Link of that music video.
            Please don't include '```json' in the result. just provide the object
        """

        prompt = f"""
            {instructions}    

            User Query: {user_query}    
        """
        response = client.models.generate_content(
            model="gemini-1.5-flash",  # Use the appropriate model
            contents=prompt
        )

        # Return the response from the model

        jsonObj=json.loads(response.text)
        print(jsonObj)
        return Response({"response": jsonObj}, status=status.HTTP_200_OK)