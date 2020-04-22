from django.contrib import admin
from .models import Desenhos

@admin.register(Desenhos)
class AdminDesenhos(admin.ModelAdmin):
	list_display = ('nome_desenho',)
	search_fields = ('nome_desenho',)
