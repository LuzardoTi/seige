from django.shortcuts import render
from users.models import Aluno, Curso, Matricula

def lista_alunos(request):
    alunos = Aluno.objects.all()
    cursos = Curso.objects.all()

    busca = request.GET.get('busca')
    curso_id = request.GET.get('curso')

    if busca:
        alunos = alunos.filter(nome__icontains=busca)

    if curso_id:
        alunos = alunos.filter(matricula__curso_id=curso_id)

    context = {
        'alunos': alunos,
        'cursos': cursos
    }

    return render(request, 'lista_alunos.html', context)

from users.models import Historico

def historico_aluno(request, aluno_id):
    historico = Historico.objects.filter(aluno_id=aluno_id)

    context = {
        'historico': historico
    }

    return render(request, 'historico_aluno.html', context)
