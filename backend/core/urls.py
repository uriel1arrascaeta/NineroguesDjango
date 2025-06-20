
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings  # Importar settings
from django.conf.urls.static import static  # Importar static

urlpatterns = [
    path('admin/', admin.site.urls),


    path('api/', include('blog.api_urls', namespace='blog_api')),


    path('django-blog/', include('blog.urls', namespace='django_blog')),
    path('accounts/', include('accounts.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns.append(
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html'), name='app'))
