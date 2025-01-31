from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError

def valitade_codigo(value):
    if not value.isalnum():
        raise ValidationError("o codigo do produto deve ter apenas letras e numeros")

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
    codigo = models.CharField(
        max_length=50,
        unique=True,
        validators=[valitade_codigo]
    )
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    quantidade_estoque = models.IntegerField(validators=[MinValueValidator(0)])  
    data_criacao = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Categoria)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def clean_nome(self):
        "validacao para conter mais de tres letras no nome"
        if self.nome < 3:
            raise ValidationError("O nome do produto deve ter pelo menos 3 caracteres.")
        return self.nome
    
    def clean_preco(self):
        if self.preco <=0:
            raise ValidationError("o preco do produto deve ser maior que 0")
        return self.preco
    
    def clean_quantidade_estoque(self):
        if self.quantidade_estoque <=0:
            raise ValidationError("quantidade deve ser maior que zero 0")
        return self.quantidade_estoque
    
    
    def __str__(self):
        return f"{self.nome} ({self.codigo})"
