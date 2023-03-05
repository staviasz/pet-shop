from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)

class MarcacaoForm(forms.Form):
    nome_pet = forms.CharField()
    telefone = forms.CharField()
    dia_reserva = forms.DateField()
    observaçoes = forms.CharField(widget=forms.Textarea)