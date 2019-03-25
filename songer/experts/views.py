from django.shortcuts import render
from .serializers import Expertserializer,RegisterExpertSerializer,ChangepasswordExpertSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import experts

# Create your views here.

class getexpertview(APIView):
    def get(self,request,format=None):
        expert = experts.objects.all()
        serializer = Expertserializer(expert,many=True)
        return Response(serializer.data)

class registerExpertsView(APIView):
    def post(self,request,format=None):
        email = request.data['email']
        is_present = experts.objects.filter(email = email)
        if(is_present):
            return Response('User already exists')
        else:
            serializer = RegisterExpertSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

class loginExpertsview(APIView):
    def post(self,request,format=None):
        email = request.data['email']
        password = request.data['password']
        loggedinuser = experts.objects.get(email=email)
        request.session['id'] = loggedinuser.id
        exp = experts.objects.filter(email=email,password=password)
        if(exp):
            return Response('Expert logged in successfully')
        else:
            return Response('Wrong credentials')


class ChangepasswordExpertView(APIView):

    def post(self,request,fromat=None):

        password = request.data['password']
        print(request.session['id'])

        #expid = request.session['expertid']

        expert = experts.objects.filter(id=1).update(password=password)
        if(expert):
            return Response('Password updated successfully')
        else:
            return Response('Error while updating password')

class UpdateExpertsView(APIView):
    def post(self,request,format=None):
        username = request.data['username']
        email = request.data['email']

        user_id = experts.objects.get(username=username)
        phone = request.data['phone']

        password = request.data['password']
        band = experts.objects.filter(id=user_id.id).update(username=username, email=email, phone=phone,
                                                              password=password)
        if (band):
            return Response('Data updated successfully!')
        else:
            return Response('Error while updating Data !')

class DeleteExpertsView(APIView):
    def post(self,request,format=None):
        email = request.data['email']
        data = experts.objects.get(email=email)
        if (data.delete()):
            return Response('User deleted successfully !!')
        else:
            return Response('Cannot delete User details .')






