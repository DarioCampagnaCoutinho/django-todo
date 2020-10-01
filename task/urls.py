from django.urls import path
from . import views


urlpatterns = [
    path('', views.list, name='list'),
    path('task/<int:id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]