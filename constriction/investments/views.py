from django.views.generic import TemplateView
from django.views.generic.list import ListView
from investments.models import Investment


class HomePageView(ListView):
    template_name = "home.html"
    model = Investment
    paginate_by = 3
    context_object_name = "investments"


class InvestmentsView(ListView):
    model = Investment
    paginate_by = 15
    context_object_name = "investments"
