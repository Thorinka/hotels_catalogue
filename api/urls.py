from django.urls import path

from .apps import ApiConfig
from .views import HotelListView

app_name = ApiConfig.name

urlpatterns = [
    path('hotels/', HotelListView.as_view(), name='hotel_list'),
]
