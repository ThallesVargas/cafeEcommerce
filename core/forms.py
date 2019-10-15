
from django import forms
from django.core.mail import send_mail
from django.conf import settings


class FaleConosco(forms.Form):

	nome = forms.CharField(label='Nome Completo', required=True)
	email = forms.EmailField(label='Email', required=True)
	mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)
	
	def __init__(self, *args, **kwargs):
		super(FaleConosco, self).__init__(*args, *kwargs)
		self.fields['nome'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['mensagem'].widget.attrs['class'] = 'form-control'

	def send_mail(self):
		nome = self.cleaned_data['nome']
		email = self.cleaned_data['email']
		mensagem = self.cleaned_data['mensagem']
		mensagem = 'Nome: {0}\nEmail: {1}\nMensagem:{2}'.format(nome, email, mensagem)
		send_mail('Contato Café Ecommerce', mensagem, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])