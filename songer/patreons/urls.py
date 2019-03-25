
from django.urls import path,include
from .views import GetPatreonsView,RegisterPatreonView,LoginPatreonView,ChangePasswordPatreonView,PostReview,UpdatePatreonView,DeletePatreonView
urlpatterns = [

    path('getdetails',GetPatreonsView.as_view()),
    path('register_patreon',RegisterPatreonView.as_view()),
    path('login_patreon',LoginPatreonView.as_view()),
    path('change_pwd',ChangePasswordPatreonView.as_view()),
    path('post_review',PostReview.as_view()),
    path('updatepatreonsdata',UpdatePatreonView.as_view()),
    path('deletepatreonsdata',DeletePatreonView.as_view())

]