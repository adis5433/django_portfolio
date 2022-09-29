from django.test import TestCase,Client
from posts.models import Post, Author
from posts.forms import PostForm
# Create your tests here.



class PostsViewsTest(TestCase):

    def setUp(self):
        Post.objects.create(title="Client test", content="raz,dwa,trzy")
        self.client = Client()

    def test_post_list(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts"]), 1)
        self.assertIn('<li><a href="/posts/1/">Client test</a></li>', response.content.decode())

class AuthorsViewsTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="Author_test", email="razdwatrzy@123.com")
        self.client = Client()

    def test_post_list(self):
        response = self.client.get("/authors/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["authors"]), 1)
        self.assertIn('<li><a href="/authors/1/">Author_test</a></li>', response.content.decode())

class PostsViewsPaginationTest(TestCase):
   fixtures = ['posts', 'authors']

   def setUp(self):
       self.client = Client()

   def test_get_first_5(self):
       response = self.client.get("/posts/")
       self.assertEqual(response.status_code, 200)
       self.assertEqual(len(response.context["posts"]), 5)

   def test_get_last_page(self):
        response = self.client.get("/posts/?page=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts"]), 1)