from django.contrib import admin
from . models import Movies

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
	list_display = ('movie_name', 'movie_categoria')
	search_fields = ('movie_name',)
