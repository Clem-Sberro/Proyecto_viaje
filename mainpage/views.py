from django.shortcuts import redirect, render
from django.views import View


class Home(View):
    template_name = 'home.html'

    def get(self, request):
        return render(
            request,
            self.template_name)
