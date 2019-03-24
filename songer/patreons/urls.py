
from django.urls import path,include
from .views import GetPatreonsView,RegisterPatreonView,LoginPatreonView,ChangePasswordPatreonView
urlpatterns = [

    path('getdetails',GetPatreonsView.as_view()),
    path('register_patreon',RegisterPatreonView.as_view()),
    path('login_patreon',LoginPatreonView.as_view()),
    path('change_pwd',ChangePasswordPatreonView.as_view())
]