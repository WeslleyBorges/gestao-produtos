from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm, CategoriaForm
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from reportlab.pdfgen import canvas

# Create your views here.
@login_required
def lista_produtos(request):
  produtos = Produto.objects.all()
  return render(request, 'produtos.html', {'produtos': produtos})

@login_required
def novo_produto(request):
  form = ProdutoForm(request.POST or None, request.FILES or None)

  if form.is_valid():
    form.save()
    return redirect('lista_produtos')
    
  return render(request, 'form-produto.html', {'form': form})

@login_required
def atualizar_produto(request, id):
  produto = get_object_or_404(Produto, pk=id)
  form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

  if form.is_valid():
    form.save()
    return redirect('lista_produtos')

  return render(request, 'form-produto.html', {'form': form})

@login_required
def excluir_produto(request, id):
  produto = get_object_or_404(Produto, pk=id)

  produto.delete()

  return redirect('lista_produtos')

def nova_categoria(request):
  form = CategoriaForm(request.POST or None, request.FILES or None)
  
  if form.is_valid():
    form.save()
    return redirect('lista_produtos')

  return render(request, 'form-categoria.html', {'form': form})