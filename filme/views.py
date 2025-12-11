from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.shortcuts import get_object_or_404
from .models import Filme, Episodio, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .forms import CriarContaForm, FormHomepage
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordChangeView





# =====================================================================
# HOMEPAGE
# =====================================================================
class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage  # ADICIONADO!

    def get(self, request, *args, **kwargs):
        # se o usuário estiver logado → manda pra HomeFilmes
        if request.user.is_authenticated:
            return redirect("filme:homefilmes")

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lista_filmes_recentes"] = Filme.objects.order_by('-data_criacao')[:6]
        return context

    def form_valid(self, form):
        email = form.cleaned_data["email"]

        usuario = User.objects.filter(email=email).first()

        # Se já existe → vai para login
        if usuario:
            return redirect("filme:login")

        # Se não existe → vai para criar conta
        return redirect("filme:criarconta")



# =====================================================================
# LISTA DE FILMES
# =====================================================================
class HomeFilmes(LoginRequiredMixin, ListView):
    model = Filme
    template_name = "homefilmes.html"
    context_object_name = "lista_filmes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["lista_filmes_recentes"] = Filme.objects.order_by('-data_criacao')[:6]
        context["lista_filmes_em_alta"] = Filme.objects.order_by('-visualizacoes')[:6]

        return context


# =====================================================================
# DETALHES DO FILME
# =====================================================================
class DetalhesFilme(LoginRequiredMixin, DetailView):
    model = Filme
    template_name = "detalhesfilme.html"

    # AULA 26 + AULA 33 (contabiliza visualização + registra como visto)
    def get(self, request, *args, **kwargs):
        filme = self.get_object()

        # Contabiliza visualização
        filme.visualizacoes += 1
        filme.save(update_fields=['visualizacoes'])

        # AULA 33 — Adiciona o filme à lista de filmes vistos pelo usuário
        if request.user.is_authenticated:
            request.user.filmes_vistos.add(filme)

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filme_atual = self.object

        # Filmes relacionados (mesma categoria)
        context["filmes_relacionados"] = (
            Filme.objects.filter(categoria=filme_atual.categoria)
            .exclude(id=filme_atual.id)[:8]
        )

        return context



# =====================================================================
# DETALHES DO EPISÓDIO
# =====================================================================
class EpisodioDetail(LoginRequiredMixin, DetailView):
    model = Episodio
    template_name = "episodio_detail.html"
    context_object_name = "episodio"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        episodio = self.object

        # Outros episódios da mesma série/filme
        context['outros_episodios'] = (
            Episodio.objects.filter(filme=episodio.filme)
            .exclude(pk=episodio.pk)
            .order_by('numero')
        )

        return context


class PesquisaFilme(LoginRequiredMixin, ListView):
    model = Filme
    template_name = "pesquisa.html"

    def get_queryset(self):
        termo = self.request.GET.get("query")

        if termo:
            return self.model.objects.filter(
                titulo__icontains=termo
            )
        return self.model.objects.none()



class PaginaPerfil(LoginRequiredMixin, UpdateView):
        model = User
        template_name = "editarperfil.html"
        fields = ["first_name", "last_name", "email"]

        def get_success_url(self):
            return reverse("filme:homefilmes")


class CriarConta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        # Cria o usuário
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        # Redireciona para o login após a criação da conta
        return reverse('filme:login')



class MudarSenha(PasswordChangeView):
    template_name = "editarperfil.html"
    success_url = reverse_lazy("filme:homefilmes")
