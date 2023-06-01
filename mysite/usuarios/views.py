from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')
    return HttpResponse(f"{nome} {senha} {email}")
