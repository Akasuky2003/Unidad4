from django.urls import path
from .views import render_public
urlpatterns = [
    path('',render_public,name='publicacion'),
]