from django.shortcuts import render, get_object_or_404
from .models import Produto, Categoria, Fornecedor

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'produtos/categorias.html', {'categorias': categorias})

def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'produtos/fornecedores.html', {'fornecedores': fornecedores})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produtos/detalhes.html', {'produto': produto})