
from .models import Type

def tipos(request):
	return{
		'tipos': Type.objects.all()
	}