from django.views.generic import TemplateView


class HomePageViews(TemplateView):
    template_name = 'index.html'
