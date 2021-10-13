from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Venda


class DashbordView(View):
    def dispatch(self, request, *args, **kwargs):
        """Verifica se o usuario tem permissão para ver a dashboard"""
        if not request.user.has_perm('ver_dashboard'):
            return HttpResponse('Você precisa de permisão para acessar a dashboard')

        return super(DashbordView, self).dispatch(request, *args, **kwargs)

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
