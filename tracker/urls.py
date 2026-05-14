from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('surahs/', views.surahs, name='surahs'),
    path('progress/', views.progress, name='progress'),
    path('add-entry/', views.add_entry, name='add_entry'),
]