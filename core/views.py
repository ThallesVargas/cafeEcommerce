from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Type, Product, Producer
from .forms import FaleConosco
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import  reverse_lazy

# Create your views here.

User = get_user_model()

def index(request):
	context = {
		'produtos': Product.objects.all(),
	}
	return render(request, 'index.html', context)

def index_tipo(request, slug):
	tipo = Type.objects.get(slug=slug)
	context = {
		'tipo': tipo,
		'produtos': Product.objects.filter(tipo=tipo),
	}
	return render(request, 'tipo.html', context)

def carrinho(request):
	info = 'Nome e especificação básica do produto'
	n = 2
	valor = 123.45
	context = {
		'info' : info,
		'n' : n,
		'valor' : valor,
	}
	return render(request, 'carrinho.html', context)

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

class RegistrarView(CreateView):

	form_class = UserCreationForm
	template_name = 'cadastro.html'
	model = User
	success_url = reverse_lazy('login')

def produtora(request):
	texto = 'Lead paragraph. A wonderful serenity has taken possessionof my entire soul.'
	produtora = 'nome da produtora'
	valor = 123.45
	context = {
		'produtora' : produtora, 
		'texto' : texto,
		'valor' : valor,
	}
	return render(request, 'produtora.html', context)

def cartao(request):
	return render(request, 'cartao.html')

def contato(request):
	success = False
	form = FaleConosco(request.POST or None)

	if form.is_valid():
		form.send_mail()
		success = True

	context = {
		'form': form,
		'success': success
	}
	return render(request, 'faleconosco.html', context)
