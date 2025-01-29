from django.db import models

class produtos(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome