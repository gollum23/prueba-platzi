from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.test import TestCase
import stripe

from .models import SubscriptionUserData


class BasicTest(TestCase):

    def test_views(self):

        # Test if home url exist
        res = self.client.get(reverse_lazy('home:home'))
        self.assertEqual(res.status_code, 200)

        # Test if subscribe url exist
        res = self.client.get(reverse_lazy('home:subscribe'))
        self.assertEqual(res.status_code, 200)


class LoginTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='platzi', email='gollum23@gmail.com', password='platzi2016')

    # Test login with incorrect credential username
    def test_login_incorrect_username(self):
        self.assertEqual(self.client.login(username='gollum23', password='platzi2016'), False)

    # Test login with incorrect credential pass
    def test_login_incorrect_password(self):
        self.assertEqual(self.client.login(username='platzi', password='platzi'), False)

    # Test login with correct credentials
    def test_login_correct_data(self):
        self.assertTrue(self.client.login(username='platzi', password='platzi2016'))


class StripeApiTest(TestCase):

    def setUp(self):
        self.card_number_correct = 4242424242424242
        self.card_cvc_correct = 123
        self.card_number_incorrect = 4242424242424243
        self.card_cvc_incorrect = 124
        self.card_month = 6
        self.card_year = 2020
        stripe.api_key = settings.STRIPE_SECRET_KEY

    # Test get token from stripe api with incorrect data
    def test_create_token_with_incorrect_data_and_return_error(self):
        try:
            stripe.Token.create(
                card={
                    'number': self.card_number_incorrect,
                    'exp_month': self.card_month,
                    'exp_year': self.card_year,
                    'cvc': self.card_cvc_correct
                }
            )

            error_message = None
        except stripe.error.CardError as e:
            error_message = e.code

        self.assertTrue(error_message)

    # Test get token form stripe api with correct data
    def test_create_token_with_correct_data_and_return_stripe_token(self):

        try:
            stripe_token = stripe.Token.create(
                card={
                    'number': self.card_number_correct,
                    'exp_month': self.card_month,
                    'exp_year': self.card_year,
                    'cvc': self.card_cvc_correct
                }
            )
            token = stripe_token
        except stripe.error:
            token = None

        self.assertTrue(token)

    # Test make payment y get customer id
    def test_payment_and_return_customer_id(self):
        stripe_token = stripe.Token.create(
            card={
                'number': self.card_number_correct,
                'exp_month': self.card_month,
                'exp_year': self.card_year,
                'cvc': self.card_cvc_correct
            }
        )

        customer = stripe.Customer.create(
            card=stripe_token,
            email='g@platzi.com',
            description='Suscription test',
            plan='Platzi-Monthly'
        )

        self.assertTrue(customer.id)


class UserTest(TestCase):

    def setUp(self):
        self.card_number_correct = 4242424242424242
        self.card_cvc_correct = 123
        self.card_number_incorrect = 4242424242424243
        self.card_cvc_incorrect = 124
        self.card_month = '06'
        self.card_year = 2020
        stripe.api_key = settings.STRIPE_SECRET_KEY

    # Test create user with customer id
    def test_save_user_basic_and_stripe_data(self):

        stripe_token = stripe.Token.create(
            card={
                'number': self.card_number_correct,
                'exp_month': self.card_month,
                'exp_year': self.card_year,
                'cvc': self.card_cvc_correct
            }
        )

        customer = stripe.Customer.create(
            card=stripe_token,
            email='test@platzi.com',
            description='Suscription test',
            plan='Platzi-Monthly'
        )

        username = 'platzi'
        password = 'platzi2016'
        email = 't@platzi.com'
        first_name = 'diego'
        last_name = 'forero'
        customer_id = customer.id
        payment_date = datetime.utcfromtimestamp(customer.created)
        print(payment_date)
        amount = customer.subscriptions.data[0].plan.amount/100
        print(amount)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        subscription = SubscriptionUserData.objects.create(
            user=user,
            payment_date=payment_date,
            amount=amount,
            stripe_id=customer_id
        )
        get_user = User.objects.get(username='platzi')

        # Test user exist
        self.assertTrue(get_user)

        # Test subscription exist
        self.assertTrue(SubscriptionUserData.objects.filter(user=get_user))

    # Test post method create subscription view
    def test_save_post_method(self):
        res = self.client.post('/suscripcion/', data={
            'username': 'platzipost',
            'password1': 'platzi2016',
            'password2': 'platzi2016',
            'email': 'test_post@platzi.com',
            'first_name': 'diego',
            'last_name': 'forero',
            'card_number': self.card_number_correct,
            'card_name': 'diego forero',
            'card_month': self.card_month,
            'card_year': self.card_year,
            'card_cvc': self.card_cvc_correct
        })

        # If post is successful redirect to gratefulness page
        self.assertEqual(res.status_code, 302)

        # Check if user is saved
        self.assertTrue(User.objects.get(username='platzipost'))

        # Check if subscription data is saved
        user = User.objects.get(username='platzipost')
        self.assertTrue(SubscriptionUserData.objects.get(user=user))

