from .models import *
from rest_framework import serializers

class MajorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Major
        fields = ['pk','name',]



class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ['pk','name','author','description','link']

class TestbankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testbank
        fields = ['pk','name','type','reference','link']

class SubjectListSerializer(serializers.HyperlinkedModelSerializer):
    major= MajorSerializer(Major.objects.all())
    class Meta:
        model = Subject
        fields = ['pk','name','level','major']


class SubjectSerializer(serializers.ModelSerializer):
    notebooks=NotebookSerializer(many=True)
    major= MajorSerializer(Major.objects.all())
    testbanks=TestbankSerializer(many=True)
    class Meta:
        model = Subject
        fields = ['pk','subject_number','name','level','major','description','type','notebooks','testbanks']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Article
        fields=['title','link','reference','date']


