from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('negociacoes/', views.negociacoes, name='negociacoes'),
  path('dashboards/', views.dashboards, name='dashboards'),
]
