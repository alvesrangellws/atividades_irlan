from django.urls import path
from . import views 

urlpatterns = [
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
    path('<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),

    path('cadastrar/categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('cadastrar/fornecedor/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('cadastrar/produto/', views.cadastrar_produto, name='cadastrar_produto'),
]
