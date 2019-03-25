from django.shortcuts import render
from rest_framework.views import APIView
from .models import Patreon,Review
from .serializers import PatreonsSerializer,RegisterPatreonsSerializer,LoginPatreonsSerializer,ChangePasswordPatreonSerializer,ReviewSerializer
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


class PostReview(APIView):
    def post(self,request,format=None):
        if(request.session['patreonid'] == None):
            return Response('Please login to continue')
        else:
            review = request.data['review']
            pat_id = request.session['patreonid']

            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdatePatreonView(APIView):
    def post(self,request,format=None):
        username = request.data['username']
        email = request.data['email']

        user_id = Patreon.objects.get(username=username)
        phone = request.data['phone']

        password = request.data['password']
        band = Patreon.objects.filter(id=user_id.id).update(username=username, email=email, phone=phone,
                                                              password=password)
        if (band):
            return Response('Data updated successfully!')
        else:
            return Response('Error while updating Data !')

class DeletePatreonView(APIView):
    def post(self,request,format=None):
        email = request.data['email']
        data = Patreon.objects.get(email=email)
        if (data.delete()):
            return Response('User deleted successfully !!')
        else:
            return Response('Cannot delete User details .')

# class UpdateExpersView(APIView):
#     def post(self,request,format=None):
#         review = request.data['review']
#         review_id =


