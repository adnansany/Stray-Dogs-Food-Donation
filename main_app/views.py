
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"


class LoginViews(TemplateView):
    template_name = "login.html"


class SigninViews(TemplateView):
    template_name = "signin.html"


