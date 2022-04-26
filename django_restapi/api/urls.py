from unicodedata import name
from django.contrib import admin
from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
        )
from .views import MovieAPIView, MovieDetailAPIView
 
app_name = 'api'

# create the new urls.py for our rest_api_app for define path for our rest api
urlpatterns = [ 
    path('',views.routes,name='routes'),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('movie_details/', MovieAPIView.as_view()), 
    path('movie_details/<int:pk>', MovieDetailAPIView.as_view()),
  
]
