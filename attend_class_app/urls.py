from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('student/units/', views.UnitListView, name = 'attend-home'),
    path('student/unit/<int:id>', views.unit, name = 'unit'),
    path('about/', views.about, name = 'attend-about'),
    path('admin/units/', views.all_units, name = 'attend-units'),
    path('admin/unit/<int:id>/', views.units_admin, name = 'attend-units-admin'),
    path('admin/unit/<int:id>/records/', views.records, name='attend-records')
]