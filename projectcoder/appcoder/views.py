from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import Curso
from django.template import Template, Context  
# Create your views here.


def tabla_familiar(request):
    archivo= open("../projectcoder/projectcoder/templates/index.html")
    plantilla=Template(archivo.read())
    archivo.close()
    contexto=Context()
    documento=plantilla.render(contexto)
    familiar=Curso.objects.all()
   

    respuesta_nombre=""
    for familiar in familiar:
        respuesta_nombre+=f"({familiar.fullname } { familiar.edad})" + " | "
    
  
    
    return HttpResponse(respuesta_nombre,documento)
