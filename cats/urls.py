from django.urls import path
from . import views  # Import view from the current folder

# Here I have created routes of the app
urlpatterns = [
    path('', views.index),
    path('cat/says/', views.search,  name='search'),
]

