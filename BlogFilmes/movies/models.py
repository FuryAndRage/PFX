from django.db import models
from BlogFilmes.categorias.models import Categoria

class Movies(models.Model):
	movie_categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	movie_name = models.CharField('Movie', max_length=50)
	movie_url = models.TextField()
	movie_img = models.TextField()
	movie_sinopse = models.TextField()

	def __str_(self):
		return self.movie_name