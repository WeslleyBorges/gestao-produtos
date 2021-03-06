from django.contrib import admin
from django.urls import path, include
from .views import lista_produtos
from .views import novo_produto, nova_categoria
from .views import atualizar_produto
from .views import excluir_produto

urlpatterns = [
    path('lista', lista_produtos, name='lista_produtos'),
    path('form-produto', novo_produto, name='novo_produto'),
    path('form-produto/<int:id>', atualizar_produto, 
          name='atualizar_produto'),
    path('excluir-produto/<int:id>', excluir_produto, name='excluir_produto'),

    path('form-categoria', nova_categoria, name='nova_categoria')
]
