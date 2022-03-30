from rest_framework import serializers
from watchlist_app.models import Movie
import re

#def special_chars(value):
#    if not re.search('^[a-zA-Z0-9]*$', value):
#        raise serializers.ValidationError('Name contains special characters!')

class MovieSerializer(serializers.ModelSerializer):
    
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        #fields = ['id', 'name', 'description']
        #exclude = ['active']

    def get_len_name(self, object):
        return len(object.name)    

    def validate(self, obj):
        if obj['name'] == obj['description']:
            raise serializers.ValidationError("Name is the same as description!")
        return obj

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Movie name too short!")
        return value
