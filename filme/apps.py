from django.apps import AppConfig
import os



class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'


    def ready(self):
        from .models import User
        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")
        usuarios = User.objects.filter(email=email)
        if not usuarios: User.objects.create_superuser(username="admin", email=email, password=senha, is_active=True,
                                                          is_staff=True, )