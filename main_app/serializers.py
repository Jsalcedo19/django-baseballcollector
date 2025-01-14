from rest_framework import serializers
from .models import Baseball
from .models import Games
from .models import Player

class BaseballSerializer(serializers.ModelSerializer):
    game_of_the_day = serializers.SerializerMethodField() # add this line

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

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        read_only_fields = ('name',)

    


