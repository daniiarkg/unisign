from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_petition, name='create_petition'),
    path('login/', views.log_in, name='login'),
    path('register/', views.register, name='register'),
    path('search/', views.search_res, name='search'),
    path('view/<int:id>/', views.view_petition, name='view_petition'),
    path('', views.main, name='main'),
]
