from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('emprestimos/', views.emprestimos, name='emprestimos'),
  path('dashboards/', views.dashboards, name='dashboards'),
]
