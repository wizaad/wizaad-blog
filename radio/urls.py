from django.urls import path
from .views import Radio, RadioListView


urlpatterns = [
    path('', RadioListView.as_view(), name='radio_index'),
    path('<int:pk>/', RadioListView.as_view(), name='portfolio_detail'),
]
