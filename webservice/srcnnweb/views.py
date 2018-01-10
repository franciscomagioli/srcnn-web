from django.shortcuts import render
from django.http import HttpResponse
from .models import ImageControl

def index(request):
    return render(request, 'srcnnweb/index.html')

def results(request):
    lista_imagens = ImageControl.objects
    context = {'lista_imagens': lista_imagens}
    return render(request, 'srcnnweb/results.html', context)

def detail(request):
    return HttpRequest("Detalhes do Resultado")
