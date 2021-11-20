from django.shortcuts import render
from .models import Service
from rest_framework import generics
from . serializers import ServiceSerializer


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
