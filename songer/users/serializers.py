from rest_framework import serializers
from .models import UserModel
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username','email','phone','password']

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['email','password']

class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['password']
