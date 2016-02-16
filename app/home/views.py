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


# View with form to subscribe
class SubscribeView(FormView):
    template_name = 'subscribe.html'
    form_class = SubscriptionForm
    stripe.api_key = settings.STRIPE_SECRET_KEY
    success_url = reverse_lazy('home:success')

    def form_valid(self, form):
        # Collect data from form
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']

        # Get token from form using stripejs library
        token = self.request.POST.get('stripeToken', None)

        # Create customer usign token
        customer = stripe.Customer.create(
            source=token,
            email=email,
            description='Suscription test',
            plan='Platzi-Monthly'
        )

        # If customer exist create user and save needed data from stripe api.
        if customer is not None:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            # user.save()

            payment_date = datetime.utcfromtimestamp(customer.created)
            amount = customer.subscriptions.data[0].plan.amount

            SubscriptionUserData.objects.create(
                user=user,
                payment_date=payment_date,
                amount=amount,
                stripe_id=customer.id
            )
            
            return super(SubscribeView, self).form_valid(form)


# View for success subscription
class SubscribeSuccessView(TemplateView):
    template_name = 'subscribe_success.html'
