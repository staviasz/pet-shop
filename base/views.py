from django.shortcuts import render
from base.forms import ContatoForm, MarcacaoForm

def inicio(request):
    return render(request, 'index.html')

def contato(request):
    sucesso = False
    if request.method == 'GET':
        form = ContatoForm()
    else: 
        form = ContatoForm(request.POST)
        if form.is_valid():
            sucesso = True
    contexto = {
        'telefone': '(99) 99999.9999',
        'responsavel': 'Erick Staviasz',
        'form': form,
        'sucesso': sucesso
    }

    return render(request, 'contato.html', contexto)

def marcacao(request):
    sucesso = False
    if request.method == 'GET':
        form =  MarcacaoForm()
    else: 
        form =  MarcacaoForm(request.POST)
        if form.is_valid():
            sucesso = True
    contexto = {
        'form': form,
        'sucesso': sucesso
    }

    return render(request, 'marcacao.html', contexto)