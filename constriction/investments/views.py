from django.views.generic import TemplateView
from django.views.generic.list import ListView
from investments.models import BaseInvestment


class HomePageView(TemplateView):
    template_name = "home.html"


class InvestmentsView(ListView):
    model = BaseInvestment
    paginate_by = 10
