from django.contrib import admin
from .models import Produto, Categoria, Fornecedor

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'preco', 'quantidade_estoque', 'data_criacao')
    search_fields = ('codigo', 'nome')
    list_filter = ('data_criacao',)
    ordering = ('-data_criacao',)
    
admin.site.register(Produto)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    
admin.site.register(Categoria)

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    
admin.site.register(Fornecedor)
