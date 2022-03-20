from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BloggerSerializer
from .models import Blogger

class BloggerViewSet(viewsets.ModelViewSet):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer
