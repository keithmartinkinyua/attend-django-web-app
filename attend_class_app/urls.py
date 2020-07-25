from django.urls import path
from .views import UnitListView, UnitDetailView
from . import views


urlpatterns = [
    path('', UnitListView.as_view(), name = 'attend-home'),
    path('unit/<int:pk>', views.UnitDetailView, name = 'unit-detail'),
    path('about/', views.about, name = 'attend-about'),
]