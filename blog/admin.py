from django.contrib import admin
from .models import Blogs # Significa vá até a models desta pasta do aplicativo e pegue a classe Blogs

admin.site.register(Blogs) # Eu gostaria de ver essa Model (tabela) dentro de Admin
