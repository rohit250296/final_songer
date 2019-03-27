from rest_framework import serializers
from .models import experts,ExpertReview

class Expertserializer(serializers.ModelSerializer):
    class Meta:
        model = experts
        fields = '__all__'

class RegisterExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = experts
        fields = ['username','email','phone','password']

class loginExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = experts
        fields = ['email','password']

class ChangepasswordExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = experts
        fields = ['password']

class ExpertReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertReview
        fields = '__all__'

