from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
def lista_produtos(request):
  produtos = Produto.objects.all()
  return render(request, 'produtos.html', {'produtos': produtos})

def novo_produto(request):
  form = ProdutoForm(request.POST or None, request.FILES or None)

  if form.is_valid():
    form.save()
    return redirect('lista_produtos')
    
  return render(request, 'form-produto.html', {'form': form})

def atualizar_produto(request, id):
  produto = get_object_or_404(Produto, pk=id)
  form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

  if form.is_valid():
    form.save()
    return redirect('lista_produtos')

  return render(request, 'form-produto.html', {'form': form})

def excluir_produto(request, id):
  produto = get_object_or_404(Produto, pk=id)

  produto.delete()

  return redirect('lista_produtos')