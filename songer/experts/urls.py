from django.urls import path,include
from .views import getexpertview,registerExpertsView,loginExpertsview,ChangepasswordExpertView,UpdateExpertsView,DeleteExpertsView,RegisterExpertReviewDetailsView,UpdateExpertReviewView,DeleteExpertsReview

urlpatterns = [
    path('getdetails',getexpertview.as_view()),
    path('register_experts',registerExpertsView.as_view()),
    path('login_experts',loginExpertsview.as_view()),
    path('change_pwd',ChangepasswordExpertView.as_view()),
    path('updateexpertsdata',UpdateExpertsView.as_view()),
    path('deleteexpertsdata',DeleteExpertsView.as_view()),
    path('registerexpertreviewdata',RegisterExpertReviewDetailsView.as_view()),
    path('updateexpertreviewdata',UpdateExpertReviewView.as_view()),
    path('deleteexpertreviewdata',DeleteExpertsReview.as_view())
]