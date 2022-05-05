from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, "ProyectoWebApp/home.html")


def servicios(request):

    return render(request, "ProyectoWebApp/servicios.html")


def tienda(request):

    return render(request, "ProyectoWebApp/tienda.html")


def blog(request):

    return render(request, "ProyectoWebApp/blog.html")


def contacto(request):

    return render(request, "ProyectoWebApp/contacto.html")

    