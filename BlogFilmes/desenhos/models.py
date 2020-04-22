from django.db import models

class Desenhos(models.Model):

	nome_desenho = models.CharField('Desenho', max_length=50)
	url_desenho = models.TextField()
	img_desenho = models.TextField()
	class Meta:
		verbose_name = "Desenho"
		verbose_name_plural = "Desenhos"

	def __str__(self):
		return self.nome_desenho

