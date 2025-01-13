from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Baseball
from .serializers import BaseballSerializer

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
