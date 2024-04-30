from django.urls import path
from .views import calculate_sgpa

urlpatterns = [
    path('', calculate_sgpa, name='calculate_sgpa'),
]