from django.shortcuts import render
from . models import Movies
from django.views.generic.list import ListView

class MoviesView(ListView):
	model = Movies
	template_name = 'movie_list.html'
	context_object_name = 'objects'
	paginate_by = 12
	ordering = '-id'

class MovieSearch(MoviesView):
	template_name = 'search.html'
	
	def get_queryset(self):
		qs = super().get_queryset()
		termo = self.request.GET.get('termo')

		qs = qs.filter(movie_name__icontains = termo)
		if not termo and not qs:
			return qs
		return qs


def player_movie(request, pk):
	filme = Movies.objects.get(pk=pk)
	return render(request, 'player_filme.html', {'obj':filme})
