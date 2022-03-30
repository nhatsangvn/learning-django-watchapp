from rest_framework import serializers
from watchlist_app.models import Movie
import re

def special_chars(value):
    if not re.search('^[a-zA-Z0-9]*$', value):
        raise serializers.ValidationError('Name contains special characters!')

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[special_chars])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate(self, obj):
        if obj['name'] == obj['description']:
            raise serializers.ValidationError("Name is the same as description!")
        return obj

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Movie name too short!")
        return value
