from django.contrib import admin

@admin.action(description='NF-e Emitida')
def nfe_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)

@admin.action(description='NF-e não Emitida')
def nfe_nao_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)