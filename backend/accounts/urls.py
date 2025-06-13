from django.urls import path
from . import views
from django.urls import path, include
app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', include('django.contrib.auth.urls')),

]
