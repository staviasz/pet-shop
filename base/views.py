from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'index.html')


def contato(request):
    return render(request, 'contato.html')