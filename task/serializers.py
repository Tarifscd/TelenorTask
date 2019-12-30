from  rest_framework import serializers
from .models import Keyvalue

class KeyvalueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyvalue
        fields = '__all__'