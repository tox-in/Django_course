from django.urls import path
from .views import index

# Define a list of urls patterns
urlpatterns = [
    path('', index, name="index")
]
