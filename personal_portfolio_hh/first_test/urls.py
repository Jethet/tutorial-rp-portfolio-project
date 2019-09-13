from django.urls import path
from first_test import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
