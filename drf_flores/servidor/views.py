from django.shortcuts import render
from .models import Flor
from .serializers import FlorSerializer
from rest_framework import generics


class FloreViewSet(generics.ListCreateAPIView):
    queryset = Flor.objects.all()
    serializer_class = FlorSerializer

