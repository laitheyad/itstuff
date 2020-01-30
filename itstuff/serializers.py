from .models import *
from rest_framework import serializers

class MajorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Major
        fields = ['name',]

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ['name','level','major','description','type']

class NotebookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notebook
        fields = ['name','author','description','link','subject']

class TestbankSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
        model = Testbank
        fields = ['name','type','reference','link','subject']


