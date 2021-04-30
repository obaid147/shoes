from django.urls import path, include
from clamor_app import views

urlpatterns = [
    path('', views.ind),
]
