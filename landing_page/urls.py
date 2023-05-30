from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landing-page-home'),
    path('about/', views.about, name='landing-page-about'),
]
