from django.contrib import admin
from .models import Venda
from .models import ItemDoPedido
from .actions import nfe_emitida, nfe_nao_emitida

class ItemDoPedidoInline(admin.TabularInline):
    model = ItemDoPedido


# Register your models here.
class VendaAdmin(admin.ModelAdmin):
    model = Venda
    list_display = ('id', 'pessoa', 'nfe_emitida')
    list_filter = ('pessoa__doc',)
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc',)
    readonly_fields = ('valor',)
    autocomplete_fields = ('pessoa',)
    actions = [nfe_emitida,nfe_nao_emitida]
    inlines = [ItemDoPedidoInline]


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDoPedido)
