from django.urls import path
from . import views

# Define a list of urls patterns
urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact-success'),
]