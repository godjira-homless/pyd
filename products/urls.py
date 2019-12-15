from django.urls import path
from . import views
# /products/new
# /products/1/detail

urlpatterns = [
    path('', views.index),
    path('new2', views.new2)
]