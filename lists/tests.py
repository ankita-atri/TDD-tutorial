from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

class HomePageTests(TestCase):
    def test_home_page_returns_correct_html(self):
        # request = HttpRequest()
        # response = home_page(request)
        response = self.client.get('/')

        self.assertContains(response, '<title>To-Do lists</title>')

        # sanity check that it's valid html
        self.assertContains(response, "<html")
        self.assertContains(response, "</html>")
        self.assertTemplateUsed(response, 'home.html')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

