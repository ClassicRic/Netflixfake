from django.apps import AppConfig
import os
from .models import User


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        from .models import User

        email = os.getenv("EMAIL_ADMIN")
        password = os.getenv("SENHA_ADMIN")

        if not email or not password:
            return

        # ✅ checar username (campo único)
        if User.objects.filter(username=email).exists():
            return

        User.objects.create_superuser(
            username=email,
            email=email,
            password=password,
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )