from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['POST'])
def artist_list_or_create(request):
    if request.method == "POST":
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
