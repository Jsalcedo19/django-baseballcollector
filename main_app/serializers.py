from rest_framework import serializers
from .models import Baseball
from .models import Games
from .models import Player
from django.contrib.auth.models import User # add this line to list of imports

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        read_only_fields = ('name',)

class BaseballSerializer(serializers.ModelSerializer):
    game_of_the_day = serializers.SerializerMethodField() # add this line
    players = PlayerSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Baseball
        fields = '__all__'
        read_only_fields = ('team_name',)

    def get_game_of_the_day(self, obj):
        return obj.game_of_the_day()

class GamesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Games
    fields = '__all__'
    read_only_fields = ('baseball',)



    


