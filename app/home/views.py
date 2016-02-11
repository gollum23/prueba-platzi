from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView
import stripe

from .models import SubscriptionUserData
from .forms import SubscriptionForm


class HomeView(TemplateView):
    template_name = 'home.html'


class SubscribeView(CreateView):
    template_name = 'subscribe.html'
    form_class = SubscriptionForm
    stripe.api_key = settings.STRIPE_SECRET_KEY

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

        try:
            stripe_token = stripe.Token.create(
                card={
                    'number': card_number,
                    'exp_month': card_month,
                    'exp_year': card_year,
                    'cvc': card_cvc
                }
            )
        except:
            stripe_token = None

        customer = stripe.Customer.create(
            card=stripe_token,
            email=email,
            description='Suscription test',
            plan='montlhy'
        )

        if customer.id:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            payment_date = datetime.utcfromtimestamp(self.customer.created)
            amount = self.customer.subscriptions.data[0].plan.amount/100

            SubscriptionUserData.objects.create(
                user=user,
                payment_date=payment_date,
                amount=amount,
                stripe_id=customer.id
            )
