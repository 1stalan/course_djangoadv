from django.urls import path
from .views import DashbordView

urlpatterns = [
    path('dashboard/',DashbordView.as_view(), name='dashboard'),
]