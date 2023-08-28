from django.urls import path

from posts.views import hello, IndexView, get_contacts, AboutView, PostDetailView, PostCtreatView, PostDeletView, PostUpdateView, PostListView, PostDetailAPIView

urlpatterns = [
    path("hello/", hello, name="hello-view"),
    path("", IndexView.as_view(), name="index-page"),
    path("conacts/", get_contacts, name="contacts-page"),
    path("about/", AboutView.as_view(), name="about-page"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="detailPost-page"),
    path("post/create/", PostCtreatView.as_view(), name="post-creat"),
    path("post/delete/<int:pk>/", PostDeletView.as_view(), name="post-delete"),
    path("post/update/<int:pk>/", PostUpdateView.as_view(), name="post-update"),
    path("api/posts/list", PostListView.as_view(), name="post-list"), 
    path("api/posts/<int:id>", PostDetailAPIView.as_view(), name="post-detail"), 
]