from rest_framework import serializers
from .models import Baseball

class BaseballSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baseball
        fields = '__all__'
