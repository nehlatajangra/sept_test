from rest_framework import serializers
import django_filters
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'