from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
	path('', views.MoviesView.as_view(), name='movie_list'),
	path('movie/<int:pk>/',views.player_movie, name='player_movie'),
	path('search/',views.MovieSearch.as_view(), name = 'search')
]