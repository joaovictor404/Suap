from django.contrib import admin
from .models import Aluno
from django.utils.html import format_html
# Register your models here.

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    
    def image_tag(self,obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ('nome', 'cpf', 'email', 'data_nascimento','image_tag')
    search_fields = ('nome', 'cpf', 'email', 'data_nascimento',)
    list_filter = ('nome', 'cpf', 'email', 'data_nascimento',)
