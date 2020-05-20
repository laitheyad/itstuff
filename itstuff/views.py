from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import filters

class MajorList(generics.ListCreateAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer

class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class OptinalSubjectList(generics.ListCreateAPIView):
    queryset = OptinalSubject.objects.all()
    serializer_class = OptinalSubjectListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class NotebookList(generics.ListCreateAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

class TestbankList(generics.ListCreateAPIView):
    queryset = Testbank.objects.all()
    serializer_class = TestbankSerializer

class SubjectDetail(APIView):

    def get_object(self,pk):
        return get_object_or_404(Subject,pk=pk)


    def get(self,request,pk):
        object=self.get_object(pk)
        serializer=SubjectSerializer(object)
        return Response(serializer.data)


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer