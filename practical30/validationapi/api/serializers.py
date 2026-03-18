from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters")
        return value

    class Meta:
        model = User
        fields = '__all__'