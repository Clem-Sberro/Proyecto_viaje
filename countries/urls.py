from django.urls import path
from .views import CountryListView, CountryDetailView


urlpatterns = [
    path('', CountryListView.as_view(), name='countries'),
    path('<slug:slug>/', CountryDetailView.as_view(), name='country'),
]