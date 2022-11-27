from django.urls import path
from block import views

urlpatterns = [
    path('', views.index, name='index'),
]