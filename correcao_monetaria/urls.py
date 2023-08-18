from django.urls import path
from . import views

urlpatterns = [
    # ... outras URLs ...
    path('', views.correcao_monetaria, name='correcao_monetaria'),
]
