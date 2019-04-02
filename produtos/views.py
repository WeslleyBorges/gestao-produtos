from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
def lista_produtos(request):
  produtos = Produto.objects.all()
  return render(request, 'produtos.html', {'produtos': produtos})

def novo_produto(request):
  form = ProdutoForm(request.POST or None, request.FILES or None)

  if(form.is_valid())
    form.save()
    return redirect('lista_produtos')
    
  return render(request, 'novo-produto.html', {'form': form})