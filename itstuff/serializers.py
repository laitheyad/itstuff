from .models import *
from rest_framework import serializers

class MajorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Major
        fields = ['name',]



class NotebookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notebook
        fields = ['name','author','description','link']

class TestbankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Testbank
        fields = ['name','type','reference','link']


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    major= MajorSerializer(Major.objects.all())
    notebook=NotebookSerializer(Notebook.objects.all(),many=True)
    testbank=TestbankSerializer(Testbank.objects.all(),many=True)
    class Meta:
        model = Subject
        fields = ['name','level','major','description','type','notebook','testbank']
