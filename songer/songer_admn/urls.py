from django.urls import path
from .views import GetAlbumDetailsView,GetBandDetailsView,GetGenreDetailsView,UpdateBandDetails,UpdateGenreDetailsView,DeleteBandDetailsView,DeleteGenerView,RegisterGenreView,UpdateBandMembersView,DeleteBandMembersView,UpdateAlbumDetailsView,DeleteAlbumDetailsView,RegisterNewsDetailsView


urlpatterns = [
    path('getalbumdetails',GetAlbumDetailsView.as_view()),
    path('updatebanddetails',UpdateBandDetails.as_view()),
    path('updategenredetails',UpdateGenreDetailsView.as_view()),
    path('getbanddetails',GetBandDetailsView.as_view()),
    path('getgenredetails',GetGenreDetailsView.as_view()),
    path('deletebanddetails',DeleteBandDetailsView.as_view()),
    path('deletegenredata',DeleteGenerView.as_view()),
    path('registergenredata',RegisterGenreView.as_view()),
    path('updatebandmenberdata',UpdateBandMembersView.as_view()),
    path('deletebandmemberdata',DeleteBandMembersView.as_view()),
    path('updatealbumdata',UpdateAlbumDetailsView.as_view()),
    path('deletealbumdata',DeleteAlbumDetailsView.as_view()),
    path('registernewsdata',RegisterNewsDetailsView.as_view())

    ]