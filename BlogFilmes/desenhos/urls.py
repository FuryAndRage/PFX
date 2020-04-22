from django.urls import path
from . import views

app_name = 'desenho'
urlpatterns = [
	path('',views.DesenhoListView.as_view(), name='desenho_list'),
	path('desenho/<int:pk>/', views.player_desenho, name='player_desenho')
]