from django.apps import AppConfig
import os
from django.db import IntegrityError



class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

