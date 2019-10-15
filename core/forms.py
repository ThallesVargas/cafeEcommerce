
from django import forms

class FaleConosco(forms.Form):

	nome = forms.Charfield(label='Nome', required=True)
	email = forms.Emailfield(label='Email', required=True)
	mensagem = forms.Charfield(label='Mensagem', widget=forms.Textarea)