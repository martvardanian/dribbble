from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('home/', index),
    path('contact/', contact),
    path('about/', about),
    path('post/', post)
]