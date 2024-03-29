from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('population-chart/', views.population_chart, name='population-chart'),
    path('widget/', views.widget, name='add-widget'),
]
