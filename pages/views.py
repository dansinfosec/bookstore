# Here we leverage Djangos built-in TemplateView so that only tweak is needed to specify our desired template
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"


# hello
