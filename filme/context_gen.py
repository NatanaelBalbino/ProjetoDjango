from .models import Filme


def lista_filmes_recentes(request):
    # sinal de menos no inicio da variavel data criacao indica que vai ordenar em forma decrescente
    lista_filmes_r = Filme.objects.all().order_by('-data_de_criacao')[0:10]
    return {"lista_filmes_recentes": lista_filmes_r}


def lista_filme_em_alta(request):
    lista_filmes_a = Filme.objects.all().order_by('-views')[0:10]
    return {"lista_filme_em_alta": lista_filmes_a}


def filme_destaque(request):
    if Filme.objects.all().order_by('-data_de_criacao'):
        filme = Filme.objects.all().order_by('-data_de_criacao')[0]
    else:
        filme = None
    return {"filme_destaque": filme}

