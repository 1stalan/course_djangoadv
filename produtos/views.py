from django.http import HttpResponse
from django.views import View
from .models import Produto


class ProdutoBulk(View):
    def get(self, request):
        produtos = ['banana', 'maca', 'laranja', 'limao', 'melancia']
        list_produto = []
        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produto.append(p)
        Produto.objects.bulk_create(list_produto)
        return HttpResponse('funcionou')