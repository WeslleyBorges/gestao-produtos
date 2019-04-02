from django.contrib import admin
from django.urls import path, include
from .views import lista_produtos

urlpatterns = [
    path('lista', lista_produtos, name='lista_produtos'),
    path('novo-produto', novo_produto, name='novo_produto')
]
