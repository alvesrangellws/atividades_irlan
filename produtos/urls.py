from django.urls import path
from . import views 

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
    path('<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
]