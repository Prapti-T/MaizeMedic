from django.shortcuts import render
from rest_framework import generics
from .models import ContactMessage
from .serializers import ContactMessageSerializer

# Create your views here.
class ContactMessageCreateView(generics.CreateAPIView):
    queryset=ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer