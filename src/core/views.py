from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    return HttpResponse('Hola Mundo!')



def saludar_con_parametro(request):
    return HttpResponse("</h1>Hola desde django</h1>")


def saludaar_con_parametro(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"Hola {nombre} {apellido} desde django con parametros!")