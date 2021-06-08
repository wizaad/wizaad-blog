from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_home'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<category>/', views.blog_category, name='blog_category'),
    path('about', views.about, name='about'),
]
