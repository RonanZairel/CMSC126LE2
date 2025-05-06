from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from . import views

# Create your views here.
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

def home(request):
    return render(request, 'reviews/index.html')
    books = Book.objects.all()
    return render(request,'reviews/home.html', {'books': books})
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
