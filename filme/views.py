from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
'''
Estudar
# FBV - Funcion Based views -> Você cria na mão tudo que vai ocorrer
    def homepage(request):
        return render(request, 'homepage.html')
    
    
    def homefilmes(request):
        context = {}
        lista_filmes = Filme.objects.all()
        context['keyLista_filmes'] = lista_filmes
        return render(request, 'homefilmes.html', context)
# CBV - Class Based views -> Você pode herdar a maior parte das coisas
'''


# Create your views here.
class Homepage(TemplateView):
    template_name = 'homepage.html'


class Homefilmes(ListView): # ListView return object_list
    template_name = 'homefilmes.html'
    model = Filme


class DetailsFilmes(DetailView): # DetailView return object
    template_name = 'detalhesfilmes.html'
    model = Filme

    def get_context_data(self, **kwargs):
        context = super(DetailsFilmes, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context
