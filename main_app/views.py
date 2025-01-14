from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Baseball, Games, Player
from .serializers import BaseballSerializer, GamesSerializer, PlayerSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the baseball-collector api home route!'}
    return Response(content)
  
class BaseballList(generics.ListCreateAPIView):
  queryset = Baseball.objects.all()
  serializer_class = BaseballSerializer

class BaseballDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Baseball.objects.all()
  serializer_class = BaseballSerializer
  lookup_field = 'id'

class GameListCreate(generics.ListCreateAPIView):
  serializer_class = GamesSerializer

  def get_queryset(self):
    baseball_id = self.kwargs['baseball_id']
    return Games.objects.filter(baseball_id=baseball_id)

  def perform_create(self, serializer):
    baseball_id = self.kwargs['baseball_id']
    baseball = Baseball.objects.get(id=baseball_id)
    serializer.save(baseball=baseball)

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    lookup_field = 'id'

    def get_queryset(self):
        baseball_id = self.kwargs['basebal_id']
        return Games.objects.filter(baseball_id=baseball_id)
    
class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'id'
    
