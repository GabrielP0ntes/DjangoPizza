from django.shortcuts import render
from django.http import HttpResponse


def reservas(request):
    return render(request, ('reserva.html'))
