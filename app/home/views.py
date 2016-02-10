from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class SubscribeView(TemplateView):
    template_name = 'subscribe.html'
