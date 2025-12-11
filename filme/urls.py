from django.urls import path
from .views import Homepage, HomeFilmes, DetalhesFilme, EpisodioDetail, PesquisaFilme, PaginaPerfil, CriarConta, MudarSenha
from django.contrib.auth import views as auth_views


app_name = 'filme'

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("filmes/", HomeFilmes.as_view(), name="homefilmes"),
    path("filme/<int:pk>/", DetalhesFilme.as_view(), name="detalhesfilme"),
    path("episodio/<int:pk>/", EpisodioDetail.as_view(), name="episodio_detail"),
    path("pesquisa/", PesquisaFilme.as_view(), name="pesquisa_filme"),
    path("login/", auth_views.LoginView.as_view(
        template_name="login.html"
    ), name="login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="filme:homepage"),
        name="logout"
    ),

    path("editar-perfil/<int:pk>/", PaginaPerfil.as_view(), name="editarperfil"),
    path("criar-conta/", CriarConta.as_view(), name="criarconta"),
    path("mudar-senha/", MudarSenha.as_view(), name="mudarsenha"),


]
