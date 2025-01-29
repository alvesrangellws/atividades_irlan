from django.db import models
class Categoria(models.Model):
    nome = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=30, null=False, blank=False)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Categoria)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nome} ({self.codigo})"
