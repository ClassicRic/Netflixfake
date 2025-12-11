from django.contrib import admin
from .models import Filme, Episodio
from .models import User
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)

campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {"fields": ("filmes_vistos",)})
)
UserAdmin.fieldsets = tuple(campos)


class EpisodioInline(admin.TabularInline):
    model = Episodio
    extra = 1


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "data_criacao")
    list_filter = ("categoria",)
    search_fields = ("titulo",)
    inlines = [EpisodioInline]


@admin.register(Episodio)
class EpisodioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "filme")
    search_fields = ("titulo",)
