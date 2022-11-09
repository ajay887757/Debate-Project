from rest_framework import serializers
from .models import Debate,DebateList

class DebetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Debate
        fields="__all__"
        depth=1

class DebateListSerializer(serializers.ModelSerializer):
    class Meta:
        model=DebateList
        fields="__all__"
