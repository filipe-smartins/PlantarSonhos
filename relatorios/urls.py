from django.urls import path
from . import views

urlpatterns = [
    path('', views.relatorios, name='relatorios'),
    path('recebimentos/', views.RelatorioView.as_view(), name='recebimentos'),
    path('alunos/', views.RelatorioAlunos.as_view(), name='alunos'),

]
