
from django.urls import path,include
from .views import UserView,UserRegistrationView,UserLoginView,ChangePasswordView,UpdateUserView,DeleteUserView
urlpatterns = [

    path('getdata',UserView.as_view()),
    path('register_user',UserRegistrationView.as_view()),
    path('login_user', UserLoginView.as_view()),
    path('change_pwd', ChangePasswordView.as_view()),
    path('updateuserdata',UpdateUserView.as_view()),
    path('deleteuserdata',DeleteUserView.as_view())
]