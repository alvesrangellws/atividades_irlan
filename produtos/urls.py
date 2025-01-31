from django.urls import path
from .views import (
    ProdutoListView, ProdutoCreateView, 
    CategoriaListView, CategoriaCreateView,
    FornecedorListView, FornecedorCreateView
)

urlpatterns = [
    path('', ProdutoListView.as_view(), name='listar_produtos'),
    path('cadastrar/produto/', ProdutoCreateView.as_view(), name='cadastrar_produto'),
    path('categorias/', CategoriaListView.as_view(), name='listar_categorias'),
    path('cadastrar/categoria/', CategoriaCreateView.as_view(), name='cadastrar_categoria'),
    path('fornecedores/', FornecedorListView.as_view(), name='listar_fornecedores'),
    path('cadastrar/fornecedor/', FornecedorCreateView.as_view(), name='cadastrar_fornecedor'),
]
