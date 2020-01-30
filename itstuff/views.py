from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

class MajorList(generics.ListCreateAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer

class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class NotebookList(generics.ListCreateAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

class TestbankList(generics.ListCreateAPIView):
    queryset = Testbank.objects.all()
    serializer_class = TestbankSerializer

