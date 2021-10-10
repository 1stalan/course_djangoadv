from django.urls import path
from .views import ProdutoBulk
urlpatterns = [
    path('produto_bulk/', ProdutoBulk.as_view(), name="produto_bulk"),
]