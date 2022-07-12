from rest_framework import serializers
from .models import User_Role

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Role
        fields = '__all__'
