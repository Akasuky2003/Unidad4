from django.shortcuts import render
from .models import Services
# Create your views here.
def index(request):
    servicio=Services.objects.all()
    return render(request, 'index.html',{'servicio':servicio})