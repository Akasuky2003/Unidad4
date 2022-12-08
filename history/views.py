from django.shortcuts import render
from .models import Publicacion
def render_public(request):
    publicado=Publicacion.objects.all()
    return render(request,'blog.html',{'publicado':publicado})