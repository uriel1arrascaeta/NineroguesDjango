from .serializers import PostSerializer  # Asumiendo que creaste serializers.py
from rest_framework import generics
from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
# Create your views here.


class BlogHomePageView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()  # Usar el manager 'objects'
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_slug = self.kwargs['slug']
        return context


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
