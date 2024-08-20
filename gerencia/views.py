from django.shortcuts import render
from .models import Aluno
# Create your views here.

def index(request):
    alunos = Aluno.objects.all()
    contexto = {
        'alunos': alunos
    }
    return render(request, 'gerencia/index.html', contexto)