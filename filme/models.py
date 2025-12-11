from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme", blank=True)


class Categoria(models.TextChoices):
    ACAO = "ACAO", "Ação"
    DRAMA = "DRAMA", "Drama"
    COMEDIA = "COMEDIA", "Comédia"
    FICCAO = "FICCAO", "Ficção"


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    thumb = models.ImageField(upload_to="thumb_filmes")

    visualizacoes = models.PositiveIntegerField(default=0)

    categoria = models.CharField(
        max_length=20,
        choices=Categoria.choices,
        default=Categoria.ACAO
    )

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Episodio(models.Model):
    filme = models.ForeignKey(
        Filme,
        related_name="episodios",
        on_delete=models.CASCADE
    )

    numero = models.PositiveIntegerField(default=1)
    titulo = models.CharField(max_length=100)

    # ❗ Agora é um **link** e não um arquivo
    video_url = models.URLField(
        blank=True,
        null=True,
        max_length=500,
        help_text="Cole aqui o link direto do supabase"
    )

    class Meta:
        ordering = ["numero"]

    def __str__(self):
        return f"{self.filme.titulo} — Episódio {self.numero}: {self.titulo}"
