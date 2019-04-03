from django.db import models

# Create your models here.
class Categoria(models.Model):
  codigo = models.CharField(max_length=15)
  descricao = models.CharField(max_length=30)

  def __str__(self):
    return self.descricao

class Produto(models.Model):
  codigo = models.CharField(max_length=15)
  descricao = models.CharField(max_length=50)
  preco = models.DecimalField(max_digits=7, decimal_places=2, null=True)
  categoria = models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.descricao