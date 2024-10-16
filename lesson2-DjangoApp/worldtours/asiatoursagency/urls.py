from django.urls import path
from . import views

# Define a list of urls patterns
urlpatterns = [
    path('', views.index)
]
