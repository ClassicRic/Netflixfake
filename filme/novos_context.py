from .models import Filme

# Lista de filmes recentes (ordenados da data mais nova para a mais antiga)
def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[:10]
    return {
        'lista_filmes_recentes': lista_filmes
    }


# Lista de filmes em alta (ordenados pela quantidade de visualizações)
def lista_filmes_em_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[:10]
    return {
        'lista_filmes_em_alta': lista_filmes
    }


def filme_destaque(request):
    try:
        filme = Filme.objects.order_by('-data_criacao').first()
    except:
        filme = None

    return {
        "filme_destaque": filme
    }