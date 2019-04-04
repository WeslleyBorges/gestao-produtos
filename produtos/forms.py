from .models import Produto, Categoria
from django.forms import ModelForm

class ProdutoForm(ModelForm):
  class Meta:
    model = Produto
    fields = ['codigo', 'descricao', 'preco', 'categoria']

class CategoriaForm(ModelForm):
  class Meta:
    model = Categoria
    fields = ['codigo', 'descricao']