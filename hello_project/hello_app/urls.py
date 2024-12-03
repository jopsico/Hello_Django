from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),  # Configura a URL para chamar a view
]