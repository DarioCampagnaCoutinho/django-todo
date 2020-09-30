from django.urls import path
from . import views


urlpatterns = [
    path('', views.list, name='list'),
    path('task/<int:id>/', views.detail, name='detail'),
]