from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Produto, Categoria, Fornecedor
from .forms import ProdutoForm, CategoriaForm, FornecedorForm


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/lista_produtos.html'
    context_object_name = 'produtos'
    paginate_by = 5
    
    def get_queryset(self):
        queryset = Produto.objects.all()
        nome = self.request.GET.get('nome')
        preco_min = self.request.GET.get('preco_min')
        preco_max = self.request.GET.get('preco_max')

        if preco_min and not preco_max:
            queryset = queryset.filter(preco__gte=preco_min)
        elif preco_max and not preco_min:
            queryset = queryset.filter(preco__lte=preco_max)
        elif preco_min and preco_max:
            queryset = queryset.filter(preco__gte=preco_min, preco__lte=preco_max)

        return queryset


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/form_produto.html'
    success_url = reverse_lazy('listar_produtos')


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'produtos/lista_categorias.html'
    context_object_name = 'categorias'


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'produtos/form_categoria.html'
    success_url = reverse_lazy('listar_categorias')


class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'produtos/lista_fornecedores.html'
    context_object_name = 'fornecedores'

class FornecedorCreateView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'produtos/form_fornecedor.html'
    success_url = reverse_lazy('listar_fornecedores')
