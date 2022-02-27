from django.contrib import admin
from .models import Project # Significa vá até a models desta pasta do aplicativo e pegue a classe Project

admin.site.register(Project) # Eu gostaria de ver essa Model (tabela) dentro de Admin



