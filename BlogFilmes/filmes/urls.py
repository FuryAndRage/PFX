from django.urls import path
from . import views
app_name = 'filme'
urlpatterns = [
	path('',views.FilmeList.as_view(), name = 'filme_list'),
	path('player/<int:pk>', views.player_video, name='player'),
	path('desenhos24h/',views.perna, name='desenhos')
]