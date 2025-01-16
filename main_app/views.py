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

   # add (override) the retrieve method below
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    # Get the list of toys not associated with this cat
    players_not_associated = Player.objects.exclude(id__in=instance.players.all())
    players_serializer = PlayerSerializer(players_not_associated, many=True)

    return Response({
        'cat': serializer.data,
        'toys_not_associated': players_serializer.data
    })
  
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

class AddPlayerToBaseball(APIView):
  def post(self, request, baseball_id, player_id):
    baseball = Baseball.objects.get(id=baseball_id)
    player = Player.objects.get(id=player_id)
    baseball.players.add(player)
    return Response({'message': f'Player {player.name} added to Baseball Team {baseball.team_name}'})

class RemovePlayerFromBaseball(APIView):
    def post(self, request, baseball_id, player_id):
        baseball = Baseball.objects.get(id=baseball_id)
        player = Player.objects.get(id=player_id)
        baseball.players.remove(player)
        return Response({'message': f'Player {player.name} removed from Baseball Team {baseball.team_name}'})
    

