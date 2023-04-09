from rest_framework import serializers
from .models import Beacon, Command, Log, Note

class BeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beacon
        fields = '__all__'

class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

