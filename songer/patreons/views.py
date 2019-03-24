from django.shortcuts import render
from rest_framework.views import APIView
from .models import Patreon
from .serializers import PatreonsSerializer,RegisterPatreonsSerializer,LoginPatreonsSerializer,ChangePasswordPatreonSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class GetPatreonsView(APIView):
    def get(self,request,format=None):
        patreons = Patreon.objects.all()
        serializer = PatreonsSerializer(patreons,many=True)
        return Response(serializer.data)

class RegisterPatreonView(APIView):
    def post(self,request,format=None):
        email = request.data['email']
        print(email)
        is_present = Patreon.objects.filter(email=email)
        if(is_present):
            return Response('User already exists')
        else:
            serializer = RegisterPatreonsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginPatreonView(APIView):
    def post(self,request,format=None):
        email = request.data['email']
        password = request.data['password']
        loggedinuser = Patreon.objects.get(email=email)
        print(loggedinuser.id)
        request.session['patreonid'] = loggedinuser.id
        pat = Patreon.objects.filter(email=email,password=password)
        if(pat):
            return Response('Patreon logged in successfully!!')
        else:
            return Response('Wrong credentials !!!')

class ChangePasswordPatreonView(APIView):
    def post(self,request,format=None):
        password = request.data['password']
        patid = request.session['patreonid']
        patreon = Patreon.objects.filter(id=patid).update(password=password)
        if(patreon):
            return Response('Password updated successfully!')
        else:
            return Response('Error while updating password !')
