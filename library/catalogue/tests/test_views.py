from django.test import Client, TestCase
from django.urls import reverse
from ..models import Book, Author


class BaseTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.author = Author.objects.create(name = 'Suzie')
        cls.book = Book.objects.create(title = 'work please', author = cls.author)

       
class TestModel(BaseTestCase):
    client = Client()
    def test_home(self):
        response = self.client.get(reverse('catalogue-home'))

        assert response.status_code == 200
        assert response.context['request'].path == '/catalogue/'
        assert 'home.html' in [t.name for t in response.templates]

    def test_about(self):
        response = self.client.get(reverse('catalogue-about'))

        assert response.status_code == 200
        assert response.context['request'].path == '/catalogue/about/'
        assert 'about.html' in [t.name for t in response.templates]

    def test_show(self):
        response = self.client.get(reverse('catalogue-show', args = [1]))

        assert response.status_code == 200

        assert "book" in response.context

        assert response.context['book'].author.name == 'Suzie'

        assert response.context['book'].title == 'work please'

        assert response.context['request'].path == '/catalogue/books/1/'

        assert 'show.html' in [t.name for t in response.templates]

