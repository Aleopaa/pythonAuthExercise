from django.test import TestCase
from ..models import Author, Book 

class BaseTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.author = Author.objects.create(name = 'Suzie')
        cls.book = Book.objects.create(title = 'work please', author = cls.author)

        #why does it not work with cls.test_author but works with cls.book

class TestModel(BaseTestCase):

    def test_author(self):
        new_author = Author.objects.get(name = 'Suzie').name

        assert new_author == 'Suzie'

    def test_book(self):
        new_book = Book.objects.get(title = 'work please')

        new_book_title = new_book.title 
        new_book_author = new_book.author.name

        assert new_book_author == 'Suzie'
        assert new_book_title == 'work please'
        assert Book.objects.count() > 0

