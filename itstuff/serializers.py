from .models import *
from rest_framework import serializers
from django_filters.rest_framework import FilterSet, filters
# import rest_framework_filters as filters
class MajorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Major
        fields = ['pk','name',]



class NotebookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notebook
        fields = ['pk','name','author','description','link']

class TestbankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Testbank
        fields = ['pk','name','type','reference','link']

class SubjectListSerializer(serializers.HyperlinkedModelSerializer):
    major= MajorSerializer(Major.objects.all())
    class Meta:
        model = Subject
        fields = ['pk','name','level','major']


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    major= MajorSerializer(Major.objects.all())
    notebook=NotebookSerializer(Notebook.objects.all(),many=True)
    testbank=TestbankSerializer(Testbank.objects.all(),many=True)
    class Meta:
        model = Subject
        fields = ['pk','name','level','major','description','type','notebook','testbank']

#
# class SubjectFilter(filters.FilterSet):
#     class Meta:
#         model = Subject
#         fields = {'name': ['exact', 'in', 'startswith']}
