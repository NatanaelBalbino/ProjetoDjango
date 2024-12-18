from django.urls import path, include
from .views import Homefilmes, Homepage, DetailsFilmes, PesquisaFilme


app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', DetailsFilmes.as_view(), name='detalhesfilmes'),
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisafilme')
]
