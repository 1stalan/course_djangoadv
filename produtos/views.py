from time import timezone
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


from .models import Produto

class ProdutoHome(ListView):
    model = Produto
    template_name = 'produtos/produtos_home.html'

class ProdutoDetail(DetailView):
    model = Produto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ProdutoCreate(CreateView):
    model = Produto
    fields = ['descricao','preco']
    success_url = reverse_lazy('produtos')

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['descricao', 'preco']
    success_url = reverse_lazy('produtos')


class ProdutoDelete(DeleteView):
    model = Produto

    success_url = reverse_lazy('produtos')

class ProdutoBulk(View):
    def get(self, request):
        produtos = ['banana', 'maca', 'laranja', 'limao', 'melancia']
        list_produto = []
        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produto.append(p)
        Produto.objects.bulk_create(list_produto)
        return HttpResponse('funcionou')