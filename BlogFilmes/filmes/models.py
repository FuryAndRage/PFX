from django.db import models
from BlogFilmes.categorias.models import Categoria

class Filmes(models.Model):
	categorias_filme = models.ForeignKey(Categoria, null = True, on_delete = models.CASCADE)
	nome_filme = models.CharField('Filme',max_length = 255)
	img_filme = models.TextField(null=True)
	url_filme = models.TextField()
	sinopse_filme = models.TextField()
	
	def __str__(self):
		return self.nome_filme

		
