from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import Country

class CountryListView(ListView):
    model = Country
    paginate_by = 20


class CountryDetailView(DetailView):
    model = Country


class CountryDeleteView(DeleteView):
    model = Country
    success_url = reverse_lazy('countries:country')