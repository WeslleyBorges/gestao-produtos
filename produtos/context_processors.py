from .models import Produto 

def produtos_dropdown(request):
  return {
    'produtos': Produto.objects.all()
  }