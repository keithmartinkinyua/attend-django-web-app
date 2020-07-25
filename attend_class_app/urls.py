from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.UnitListView, name = 'attend-home'),
    path('unit/<int:pk>', views.UnitDetailView.as_view(), name = 'unit-detail'),
    path('about/', views.about, name = 'attend-about'),
]