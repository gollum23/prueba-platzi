from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView
import stripe

from .models import SubscriptionUserData
from .forms import SubscriptionForm


# Home Page
class HomeView(TemplateView):
    template_name = 'home.html'


# Page with form to suscribe
class SubscribeView(FormView):
    template_name = 'subscribe.html'
    form_class = SubscriptionForm
    stripe.api_key = settings.STRIPE_SECRET_KEY
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        # Collect data from form
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        card_number = form.cleaned_data['card_number']
        card_month = form.cleaned_data['card_month']
        card_year = form.cleaned_data['card_year']
        card_cvc = form.cleaned_data['card_cvc']

        # Try get token form stripe api, if fail, send messages and trigger form_invalid function
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
            messages.error(self.request, 'Verifique los datos de su tarjeta de credito')
            return self.form_invalid(form)

        # If stripe_token exist, create customer using stripe api, else customer is None
        if stripe_token:
            customer = stripe.Customer.create(
                card=stripe_token,
                email=email,
                description='Suscription test',
                plan='Platzi-Monthly'
            )
        else:
            customer = None

        # If customer exist create user and save needed data from stripe api.
        if customer is not None:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            payment_date = datetime.utcfromtimestamp(customer.created)
            amount = customer.subscriptions.data[0].plan.amount/100

            SubscriptionUserData.objects.create(
                user=user,
                payment_date=payment_date,
                amount=amount,
                stripe_id=customer.id
            )
            
            return super(SubscribeView, self).form_valid(form)
