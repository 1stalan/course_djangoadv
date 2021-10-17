from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Person
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.utils import timezone


# Class bases Views

class PersonList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Person
    template_name = 'person_list.html'

    # Verifica se o usuario tem permissão de ver a lista de clientes
    permission_required = ('clientes.view_person',)


class PersonDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Person
    # Verifica se o usuario tem permissão de ver a lista de clientes
    permission_required = ('clientes.view_person',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/person_list'


class PersonUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list')

    # Verifica se o usuario tem permissão de ver a alterar os dados do clientes
    permission_required = ('clientes.change_person',)


class PersonDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('person_list')
    # Verifica se o usuario tem permissão de deletar um cliente do banco
    permission_required = ('clientes.deletar_clientes',)
