from django.contrib import admin
from .models import Filmes


@admin.register(Filmes)
class FilmesAdmin(admin.ModelAdmin):

	list_display = ('__str__','nome_filme',)
	search_fields = ('nome_filme',)

