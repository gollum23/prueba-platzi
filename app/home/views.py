from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView
import stripe

from .forms import SubscriptionForm


class HomeView(TemplateView):
    template_name = 'home.html'


class SubscribeView(CreateView):
    template_name = 'subscribe.html'
    form_class = SubscriptionForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        card_number = form.cleaned_data['card_number']
        card_month = form.cleaned_data['card_month']
        card_year = form.cleaned_data['card_year']
        card_cvc = form.cleaned_data['card_cvc']

        user = User.objects.create_user(
            username=username, email=email, password=password)

        user.first_name = first_name
        user.last_name = last_name
        user.save()
