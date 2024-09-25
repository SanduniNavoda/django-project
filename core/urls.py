from django.urls import path 
from .views import visualize_data

urlpatterns = [
    path('visualize/', visualize_data, name='visualize_data'),
]

