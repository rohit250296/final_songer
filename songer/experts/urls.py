from django.urls import path,include
from .views import getexpertview,registerExpertsView,loginExpertsview,ChangepasswordExpertView,UpdateExpertsView,DeleteExpertsView

urlpatterns = [
    path('getdetails',getexpertview.as_view()),
    path('register_experts',registerExpertsView.as_view()),
    path('login_experts',loginExpertsview.as_view()),
    path('change_pwd',ChangepasswordExpertView.as_view()),
    path('updateexpertsdata',UpdateExpertsView.as_view()),
    path('deleteexpertsdata',DeleteExpertsView.as_view())
]