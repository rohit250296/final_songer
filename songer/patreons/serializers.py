from rest_framework import serializers
from .models import Patreon
class PatreonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patreon
        fields ='__all__'
class RegisterPatreonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patreon
        fields = ['username','email','phone','password']

class LoginPatreonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patreon
        fields = ['email','password']

class ChangePasswordPatreonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patreon
        fields = ['password']