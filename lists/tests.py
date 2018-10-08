from django.test import TestCase



from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item

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

    def test_uses(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_only_save(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
        # self.assertIn('A new list item', response.content.decode())
        # self.assertTemplateUsed(response, 'home.html')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_display_all(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        response = self.client.get('/')
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())


    class ItemModelTest(TestCase):

        def test_save(self):
            pass


