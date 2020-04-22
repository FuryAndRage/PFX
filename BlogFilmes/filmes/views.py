from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Filmes
def index(request):
	return render(request, 'base.html')

class FilmeList(ListView):
	model = Filmes
	template_name = 'catalogo.html'
	context_object_name = 'objects'



def player_video(request, pk):
	filme = Filmes.objects.get(pk=pk)
	print(filme.url_filme)
	return render(request, 'player.html',{'obj':filme})

def perna(request):
	return render(request, 'perna.html')
