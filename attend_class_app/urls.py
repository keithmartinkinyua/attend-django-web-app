from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.UnitListView, name = 'attend-home'),
    path('unit/<int:id>', views.unit, name = 'unit'),
    path('about/', views.about, name = 'attend-about'),
    path('units/', views.all_units, name = 'attend-units'),
    path('unit/<int:id>/admin/', views.units_admin, name = 'attend-units-admin'),
    path('unit/<int:id>/admin/records/', views.records, name='attend-records')
]