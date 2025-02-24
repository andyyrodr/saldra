from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    return HttpResponse('Hola Mundo!')



def saludar_con_parametro(request):
    return HttpResponse("</h1>Hola desde django</h1>")
