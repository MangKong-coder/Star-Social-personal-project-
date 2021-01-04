from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"


class Test(TemplateView):
    template_name = "test.html"


class Thanks(TemplateView):
    template_name = "thanks.html"


