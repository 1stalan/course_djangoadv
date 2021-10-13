from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('clientes/', include('clientes.urls')),
    path('produtos/', include('produtos.urls')),
    path('vendas/', include('vendas.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('home.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Gestão de clientes'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Bem-Vindo a Gestão de clientes'