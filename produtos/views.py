from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Categoria, Fornecedor
from .forms import ProdutoForm, CategoriaForm, FornecedorForm

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'produtos/lista_categorias.html', {'categorias': categorias})

def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'produtos/lista_fornecedores.html', {'fornecedores': fornecedores})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produtos/detalhes.html', {'produto': produto})

def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'produtos/form_categoria.html', {'form': form})

def cadastrar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm()
    return render(request, 'produtos/form_fornecedor.html', {'form': form})

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/form_produto.html', {'form': form})
