from django.db import models


# Create your models here.
class Major(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Testbank(models.Model):
    name=models.CharField(max_length=150)
    reference=models.CharField(max_length=150,null=True)
    type=models.CharField(max_length=50,null=True)
    #subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    link=models.URLField(max_length=600)
    def __str__(self):
        return self.name

class Notebook(models.Model):
    name=models.CharField(max_length=150)
    author=models.CharField(max_length=150)
    description=models.TextField(null=True)
    # subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    link=models.URLField(max_length=600)
    def __str__(self):
        return self.name

class Subject(models.Model):
    subject_number=models.CharField(max_length=10)
    name=models.CharField(max_length=150)
    level=models.IntegerField(default=1)
    type=models.CharField(max_length=50)
    description=models.TextField(blank=True,null=True)
    major=models.ForeignKey(Major,on_delete=models.CASCADE,blank=True)
    testbank=models.ManyToManyField(Testbank)
    notebook=models.ManyToManyField(Notebook)
    def __str__(self):
        return self.name
