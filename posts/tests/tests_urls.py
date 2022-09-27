
from django.test import TestCase,Client
from posts.models import Post, Author
from posts.forms import PostForm
from django.urls.exceptions import Resolver404
from posts.views import single_post, single_author
# Create your tests here.

class TestUrls(TestCase):
   def test_resolution_for_single_post(self):
       resolver = resolve('/posts/1')
       self.assertEqual(resolver.func, single_post)

   def test_resolution_for_single_author(self):
       resolver = resolve('authors/2')
       self.assertEqual(resolver.func, sub)

   def test_id_of_element_is_in_list_or_404(self):
       with self.assertRaises(Resolver404):
           resolve('authors/0')