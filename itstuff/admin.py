from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources


#Major
class MajorResource(resources.ModelResource):

    class Meta:
        model = Major

class MajorAdmin(ImportExportModelAdmin):
    resource_class = MajorResource


#Subject
class SubjectResource(resources.ModelResource):

    class Meta:
        model = Subject

class SubjectAdmin(ImportExportModelAdmin):
    resource_class = SubjectResource


#Notebook
class NotebookResource(resources.ModelResource):

    class Meta:
        model = Notebook

class NotebookAdmin(ImportExportModelAdmin):
    resource_class = NotebookResource


#Testbank
class TestbankResource(resources.ModelResource):

    class Meta:
        model = Testbank

class TestbankAdmin(ImportExportModelAdmin):
    resource_class = TestbankResource

class ArticleResource(resources.ModelResource):

    class Meta:
        model = Article

class ArticlerAdmin(ImportExportModelAdmin):
    resource_class = ArticleResource


admin.site.register(Major, MajorAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Testbank, TestbankAdmin)
admin.site.register(Article,ArticlerAdmin)
# # Register your models here.
# admin.site.register(Subject)
# # admin.site.register(Notebook)
# admin.site.register(Testbank)
# admin.site.register(Major)
