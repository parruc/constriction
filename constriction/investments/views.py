from django.views.generic import TemplateView
from django.views.generic.list import ListView
from investments.models import Investment


class HomePageView(TemplateView):
    template_name = "home.html"


class InvestmentsView(ListView):
    model = Investment
    paginate_by = 10
