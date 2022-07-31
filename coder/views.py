from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Curso,Estudiante,Profesor,Entregable
# Create your views here.
def cursos(request):
    
    curso = Curso.objects.all()
    lista_cursos_nombres = []
    for curso in cursos:
        lista_cursos_nombres.append(curso.nombre)
        return HttpResponse(lista_cursos_nombres)
    

def inicio(request):
    return render(request,"coder/index.html",{"mensaje":"La comision es la mejor"})

def estudiante(request):
    return HttpResponse("Vista de estudiante")

def profesor(request):
    return HttpResponse("Vista de profesor")

def entregable(request):
    return HttpResponse("Vista de entregable")