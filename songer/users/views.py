from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from .models import UserModel
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer,UserRegistrationSerializer,UserLoginSerializer,ChangePasswordSerializer
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserView(APIView):
    def get(self,request,format=None):
        users = UserModel.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

class UserRegistrationView(APIView):
    def post(self,request,format=None):
        email = request.data['email']
        is_user_present = UserModel.objects.filter(email=email)
        if(is_user_present):
            return Response('User already registered !!')
        else:
            serializer = UserRegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self,request,format=None):
        email = request.data['email']
        password = request.data['password']
        print(email)
        print(password)
        user2 = get_object_or_404(UserModel,email=email)
        print(user2.id)
        request.session['userid'] = user2.id
        print(request.session['userid'])
        # if email is None:
        #     return Response('Please provide an email')
        # if password is None:
        #     return Response('Please provide password')
        user = get_object_or_404(UserModel,email =email,password=password)
        if(user):
            print()
            return Response('Logged in successfully')
        else:
            return Response('User not present')
        # user = UserLoginSerializer(email,password)
        # if user.is_valid():
        #     if(user):
        #         return Response(user.data, status=status.HTTP_201_CREATED)
        #     else:
        #         return Response('User not present')

class ChangePasswordView(APIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        pwd = request.data['password']
        id = request.session['userid']
        user = UserModel.objects.filter(id=id).update(password=pwd)
        if(user):
            return Response('Password changed successfully')
        else:
            return Response('Cannot change the password ')

class UpdateUserView(APIView):
    def post(self,request,format=None):
        username = request.data['username']
        email = request.data['email']


        user_id = UserModel.objects.get(username=username)
        phone = request.data['phone']

        password = request.data['password']
        band = UserModel.objects.filter(id=user_id.id).update(username = username,email=email,phone=phone,password=password)
        if (band):
            return Response('Data updated successfully!')
        else:
            return Response('Error while updating Data !')

class DeleteUserView(APIView):
    def post(self,request,format=None):
        email = request.data['email']
        data = UserModel.objects.get(email=email)
        if (data.delete()):
            return Response('User deleted successfully !!')
        else:
            return Response('Cannot delete User details .')
