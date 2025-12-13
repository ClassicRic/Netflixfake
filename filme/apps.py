from django.apps import AppConfig
import os


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        from .models import User

        email = os.getenv("EMAIL_ADMIN")
        password = os.getenv("SENHA_ADMIN")

        if not email or not password:
            return

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(
                username=email,
                email=email,
                password=password,
                is_active=True,
                is_staff=True,
                is_superuser=True,
            )
