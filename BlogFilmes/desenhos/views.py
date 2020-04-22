from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Desenhos

class DesenhoListView(ListView):
	model = Desenhos
	context_object_name = 'objects'
	template_name = 'desenhos.html'

def player_desenho(request, pk):
	desenho = Desenhos.objects.get(pk=pk)
	return render(request, 'player_desenho.html',{'obj':desenho})