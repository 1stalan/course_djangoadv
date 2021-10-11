from django.shortcuts import render
from django.views import View
from .models import Venda


class DashbordView(View):
    def get(self, request):
        data = {}
        data['media'] = Venda.objects.media()
        data['media_desc'] = round(Venda.objects.media_desc(), 2)
        data['min'] = Venda.objects.min()
        data['max'] = Venda.objects.max()
        data['n_ped'] = Venda.objects.n_ped()
        data['n_ped_nfe'] = Venda.objects.n_ped_nfe()

        print(data)

        return render(request, 'vendas/dashboard.html', data)
