from django.contrib import admin
from .models import Person, Documento, Venda, Produto

admin.site.enable_nav_sidebar = False

admin.site.register(Person)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)
