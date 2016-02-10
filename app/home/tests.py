from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.test import TestCase


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

    # Test login with subscription active (between thirty days from last payment)

    # Test login with subscription defeated (after thirty one days from last payment)


class SubscribeTest(TestCase):

    def setUp(self):
        self.card_number_correct = 4242424242424242
        self.card_csv_correct = 123
        self.card_number_incorrect = 4242424242424243
        self.card_csv_incorrect = 124
        self.card_month = 6
        self.card_year = 2020

    # Test create user with data correct

    # Test create user with data incorrect

