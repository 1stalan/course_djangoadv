from django.contrib import admin
from .models import Person, Documento, Venda
from .models import ItensDoPedido

admin.site.enable_nav_sidebar = False


class PersonAdmin(admin.ModelAdmin):
    model = Person
    fields = ('first_name', 'last_name', 'age', 'salary', 'bio', 'photo', 'doc')
    list_filter = ('age', 'salary')
    list_display = ('full_name', 'age', 'has_photo')
    search_fields = ('first_name', 'last_name', 'age')

    def full_name(self, obj):
        name = obj.first_name + ' ' + obj.last_name
        return name

    full_name.short_description = 'Nome Completo'

    def has_photo(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'

    has_photo.short_description = 'Tem Foto'


class DocumentoAdmin(admin.ModelAdmin):
    model = Documento
    search_fields = ['num_doc']


class VendaAdmin(admin.ModelAdmin):
    model = Venda
    list_display = ('id', 'pessoa')
    list_filter = ('pessoa__doc',)
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc',)
    readonly_fields = ('valor',)
    autocomplete_fields = ['pessoa']



admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(ItensDoPedido)
