from django.contrib import admin
from . models import *

class ModuloVertical(admin.StackedInline):
    model=Modulos
    extra=1
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines=[ModuloVertical]

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display=('nome','email')
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display=('nome','email')
admin.register(Modulos)

@admin.register(Inscricoes)
class InscricaoAdmin(admin.ModelAdmin):
    list_display=(
        'aluno',
        'curso',
        'data_inscricao'
    )
@admin.register(Avaliacao)
class avaliacaoAdmin(admin.ModelAdmin):
    list_display=(
        'aluno',
        'curso',
        'nota',
        'data'
    )