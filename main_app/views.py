from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from .models import Baseball, Games, Player
from .serializers import BaseballSerializer, GamesSerializer, PlayerSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied # include this additional import

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the baseball-collector api home route!'}
    return Response(content)
  
class BaseballList(generics.ListCreateAPIView):
  queryset = Baseball.objects.all()
  serializer_class = BaseballSerializer
  permission_classes = [permissions.IsAuthenticated]

def get_queryset(self):
    user = self.request.user
    return Baseball.objects.filter(user=user)

def perform_create(self, serializer):
    serializer.save(user=self.request.user)


class BaseballDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Baseball.objects.all()
  serializer_class = BaseballSerializer
  lookup_field = '_id'

  def get_queryset(self):
    user = self.request.user
    return Baseball.objects.filter(user=user)
  
  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    # Get the list of toys not associated with this baseball team
    players_not_associated = Player.objects.exclude(id__in=instance.players.all())
    players_serializer = PlayerSerializer(players_not_associated, many=True)

    return Response({
        'baseball': serializer.data,
        'players_not_associated': players_serializer.data
    })
def perform_update(self, serializer):
    baseball = serializer.instance
    if baseball.user != self.request.user:
        raise PermissionDenied("You can not change this baseball team")
    serializer.save()

def perform_destroy(self, instance):
    if instance.user != self.request.user:
        raise PermissionDenied("You can not delete this baseball team")
    instance.delete()
  
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
    
class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

# User Login
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })
