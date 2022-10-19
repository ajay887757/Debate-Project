from dataclasses import fields
from pydoc import importfile
from pyexpat import model
from rest_framework import serializers
from .models import Debate

class DebetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Debate
        fields="__all__"