from django.contrib import admin
from .models import Task

@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','status','data_criacao', 'data_atualizacao', 
'data_conclusao')