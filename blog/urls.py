

from django.urls import path

from blog import views

urlpatterns = [
    path('about/', views.about,name='blog-about'),
    path('', views.home, name='blog-home')
]
