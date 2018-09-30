from django.test import TestCase



from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


class HomePageTest(TestCase):

    def test_root(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # request = HttpRequest()

        # response = home_page(request)
        response = self.client.get('/')
        # html = response.content.decode('utf-8')
        # self.assertTrue(html.startswith('<html>'))
        expected_html = render_to_string('home.html')
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.endswith('</html>'))
        # self.assertEqual(html, expected_html)
        self.assertTemplateUsed(response, 'home.html')