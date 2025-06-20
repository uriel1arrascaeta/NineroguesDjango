from django.urls import path
from .views import BlogHomePageView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CategoryCreateView

app_name = 'django_blog'
urlpatterns = [
    path('', BlogHomePageView.as_view(), name='home'),
    path('post/new/', PostCreateView.as_view(),
         name='post_create'),
    path('category/new/', CategoryCreateView.as_view(), name='category_create'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(),
         name='post_update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(),
         name='post_delete'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
