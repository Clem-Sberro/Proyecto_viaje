from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Country

class CountryListView(ListView):
    model = Country
    paginate_by = 20


class CountryDetailView(DetailView):
    model = Country