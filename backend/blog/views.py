from .serializers import PostSerializer
from rest_framework import generics
from django.shortcuts import render
from .models import Post, Category
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy
from .forms import PostForm, CategoryForm

from django.views.generic.edit import UpdateView


class BlogHomePageView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        title = form.cleaned_data['title']
        original_slug = slugify(title)

        queryset = Post.objects.all()
        slug = original_slug
        counter = 1
        while queryset.filter(slug=slug).exists():
            slug = f"{original_slug}-{counter}"
            counter += 1

        form.instance.slug = slug
        response = super().form_valid(form)
        messages.success(
            self.request, f"¡Post '{self.object.title}' creado exitosamente!")
        return response

    def get_success_url(self):
        return reverse('django_blog:post_detail', kwargs={'slug': self.object.slug})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def form_valid(self, form):
        messages.success(
            self.request, f"¡Post '{form.instance.title}' actualizado exitosamente!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('django_blog:post_detail', kwargs={'slug': self.object.slug})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('django_blog:home')
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, f"Post '{self.get_object().title}' eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'blog/category_form.html'
    success_url = reverse_lazy('django_blog:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, f"¡Categoría '{self.object.name}' creada exitosamente!")
        return response


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
