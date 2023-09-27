from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Person
from .serializers import PersonSerializer
# Create your views here.
def index(request):
    return render(request,'index.html')

def crud(request):
    return render(request,'crud.html')

def templatePage(request):
    return render(request,'bootpage.html')

def QueryPage(request):
    return render(request,'query.html')

class PersonViewset(viewsets.ModelViewSet):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    