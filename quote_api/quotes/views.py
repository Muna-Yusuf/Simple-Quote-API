from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .storage import load_quotes, save_quotes

class QuoteListAPI(APIView):
    """API view to list all quotes."""
    def get(self, request):
        """Handles GET requests to list all quotes."""

        return Response({"data": load_quotes()})
    
    def post(self, request):
        """Handles POST requests to create a new quote."""

        text = request.data.get("text", "").strip()
        author = request.data.get("author", "").strip()

        if not text or len(text) < 15:
            return Response({"error": "Quote must be at least 15 characters."}, status=400)
        if not author:
            return Response({"error": "Author is required."}, status=400)

        quote = save_quotes(text, author)
        return Response({
            "data": quote,
            "message": "Quote added successfully"
        }, status=201)
        