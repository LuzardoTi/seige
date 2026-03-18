from django.contrib import admin
from .models import Aluno, Curso, Polo, Disciplina, Matricula

admin.site.register(Aluno)
admin.site.register(Curso)
admin.site.register(Polo)
admin.site.register(Disciplina)
admin.site.register(Matricula)
