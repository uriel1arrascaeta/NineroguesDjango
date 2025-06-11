from django.urls import path
from .views import PostListAPIView, PostDetailAPIView

app_name = 'blog_api'

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostDetailAPIView.as_view(), name='post-detail'),
]
