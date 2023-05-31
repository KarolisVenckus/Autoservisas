from django.urls import path
from . import views

app_name = 'servisas'

urlpatterns = [
    path('paslaugu-ivestis/', views.paslaugu_ivestis, name='paslaugu-ivestis'),
    # Add other URL patterns for your views here
]