from django.urls import path

from users.views import UserRegister, UserListView, UserDetailAPIView

urlpatterns = [
    path("users/register/", UserRegister.as_view(), name="register"),   
    path("api/users/list", UserListView.as_view(), name="post-list"), 
    path("api/users/<int:id>", UserDetailAPIView.as_view(), name="post-detail"),  
]