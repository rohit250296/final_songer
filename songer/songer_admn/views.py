from django.shortcuts import render
from .serializers import AlbumSerializer,BandSerializer,GenreSerializer,RegisterGenreSerializer
from .models import Album,Band,Genre
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

class GetAlbumDetailsView(APIView):
    def get(self,request,format=None):
        album = Album.objects.all()
        serializer = AlbumSerializer(album,many=True)
        return Response(serializer.data)

class UpdateBandDetails(APIView):
    def post(self,request,format=None):

        name2 = request.data['name']
        description2 = request.data['description']
        print(description2)
        print(request.data['formed'])
        bandid = Band.objects.get(name=name2)
        formed2 = request.data['formed']
        image_url2 = request.data['image_url']
        website_url2 = request.data['website_url']
        band = Band.objects.filter(band_id=bandid.band_id).update(name=name2,description=description2,formed=formed2,image_url=image_url2,website_url=website_url2)
        if (band):
            return Response('Data updated successfully!')
        else:
            return Response('Error while updating Data !')


class GetBandDetailsView(APIView):
    def get(self,request,format=None):
        band = Band.objects.all()
        serializer = BandSerializer(band,many=True)
        return Response(serializer.data)

class GetGenreDetailsView(APIView):
    def get(self,request,format=None):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre,many=True)
        return Response(serializer.data)

class RegisterGenreView(APIView):
    def post(self,request,format=None):
       # genre_name = request.data['genre']
        serializer = RegisterGenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateGenreDetailsView(APIView):
    def post(self,request,format=None):
        name = request.data['name']

        genre_id = Genre.objects.get(genre_name=name)
        updated_data = Genre.objects.filter(genre_id = genre_id).update(genre_name = name)
        if(updated_data):
            return Response('Data updated successfully!')
        else:
            return Response('Error while updating Data !')

class DeleteBandDetailsView(APIView):
    def post(self,request,format=None):
        name = request.data['name']
        data = Band.objects.get(name=name)
        if(data.delete()):
            return Response('Band deleted successfully !!')
        else:
            return Response('Cannot delete Band details .')

class DeleteGenerView(APIView):
    def post(self,request,format=None):
        name2 = request.data['genre_name']
        data = get_object_or_404(Genre,genre_name=name2)
        if(data.delete()):
            return Response('Genre deleted successfully !!')
        else:
            return Response('Cannot delete Genre details .')


