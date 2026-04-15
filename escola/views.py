from django.shortcuts import render
from .models import Curso, Professor, Aluno
# Create your views here.
def cursos_view(request):
    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()    
    return render(request, 'escola/cursos.html', {'cursos': cursos})

def professors_view(request):
    professores = Professor.objects.prefetch_related('cursos').all()
    return render(request, 'escola/professores.html', {'professores': professores})

def alunos_view(request):
    alunos = Aluno.objects.prefetch_related('cursos').all()
    return render(request, 'escola/alunos.html', {'alunos': alunos})