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
