from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context   


def vista_saludo(request):
    return HttpResponse("hola mundo")

def login(request):
    return HttpResponse("Ingrese su contraseña: ")

def dia_hoy(request, nombre):
    hoy = datetime.year
    edad=int(edad)
    
    respuesta=f"hoy es {hoy} - Bienvenid@ {nombre} "
    return HttpResponse(respuesta)

def edadnac(request, edad):
    
    edad=int(edad)
    edad1=datetime.now().year - edad
    respuesta=f"su edad es {edad1}"
    return HttpResponse(respuesta)

def vista_plantilla(request):
    archivo= open("C:/Users/sebas/OneDrive/Escritorio/Django_project/projectcoder/projectcoder/templates/index.html")
    plantilla=Template(archivo.read())
    archivo.close()
    datos={"nombre": "Sebas", "fecha": datetime.now(), "apellido":"Murcia"}
    contexto=Context(datos)
    documento=plantilla.render(contexto)
    return HttpResponse(documento)