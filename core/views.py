from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	texto = 'Lead paragraph. A wonderful serenity has taken possessionof my entire soul.'
	produtora = 'nome da produtora'
	valor = 123.45
	context = {
		'produtora' : produtora, 
		'texto' : texto,
		'valor' : valor
	}
	return render(request, 'index.html', context)

def carrinho(request):
	return render(request, 'carrinho.html')

def inicial(request):
	return render(request, 'inicial.html')

def busca(request):
	produtora = 'nome da produtora'
	valor = 123.45
	context = {
		'produtora' : produtora,
		'valor' : valor,
	}
	return render(request, 'busca.html', context)

def cadastro(request):
	return render(request, 'cadastro.html')

def login(request):
	return render(request, 'login.html')

def produtora(request):
	produtora = 'nome da produtora'
	context = {
		'produtora' : produtora,
	}
	return render(request, 'produtora.html', context)

def cartao(request):
	return render(request, 'cartao.html')