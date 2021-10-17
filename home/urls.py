from django.urls import path, include
from .views import home
from .views import MyLogout



urlpatterns = [
    path('', home, name="home"),
    path('logout/', MyLogout.as_view(), name='logout'),
]