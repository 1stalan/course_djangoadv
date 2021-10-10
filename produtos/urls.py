from django.urls import path
from .views import ProdutoBulk
from .views import ProdutoHome
from .views import ProdutoCreate
from .views import ProdutoUpdate
from .views import ProdutoDelete
urlpatterns = [
    path('list/', ProdutoHome.as_view(), name="produtos"),
    path('produto_create/', ProdutoCreate.as_view(), name="produto_create"),
    path('produto_update/<int:pk>/', ProdutoUpdate.as_view(), name="produto_update"),
    path('produto_delete/<int:pk>/', ProdutoDelete.as_view(), name="produto_delete"),
    path('produto_bulk/', ProdutoBulk.as_view(), name="produto_bulk"),

]