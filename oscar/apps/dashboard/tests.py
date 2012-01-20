import httplib

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()


class AnonymousUserTests(ViewTests):

    def test_login_form_is_displayed_for_anon_user(self):
        response = self.client.get(reverse('dashboard:index'))
        self.assertTrue('Username' in response.content)


class StaffViewTests(ViewTests):

    def setUp(self):
        super(StaffViewTests, self).setUp()
        user = User.objects.create_user('staffperson', 'staff@example.com', 'staffpassword')
        user.is_staff = True
        user.save()
        self.client.login(username='staffperson', password='staffpassword')


class DashboardViewTests(StaffViewTests):

    def test_dashboard_index_is_for_staff_only(self):
        urls = ('dashboard:index',
                'dashboard:orders',)
        for name in urls:
            response = self.client.get(reverse(name))
            self.assertTrue('Username' not in response.content)


class OrderListTests(StaffViewTests):

    def test_searching_for_valid_order_number_redirects_to_order_page(self):
        pass


