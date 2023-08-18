from django.urls import path
from . import views

urlpatterns = [
    # ... outras URLs ...
    path('', views.cobranca_adicional, name='cobranca_adicional'),
]
