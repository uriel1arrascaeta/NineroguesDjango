
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),


    path('api/', include('blog.api_urls', namespace='blog_api')),

    path('django-blog/', include('blog.urls', namespace='django_blog')),

    re_path(r'^.*$', TemplateView.as_view(template_name='index.html'), name='app'),
]
