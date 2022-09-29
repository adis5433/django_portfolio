
from django.test import TestCase,Client
from posts.models import Post, Author
# Create your tests here.


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="testing_case", content="testing_post_model")
        Post.objects.create(title="testing_case_2", content="testing_post_model_2")

    def test_posts_str(self):

        p1 = Post.objects.get(title="testing_case")
        p2 = Post.objects.get(title="testing_case_2")

        self.assertEqual(p1.title, "testing_case")
        self.assertEqual(p1.content, "testing_post_model")
        self.assertEqual(p2.title, "testing_case_2")
        self.assertEqual(p2.content, "testing_post_model_2")

class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="modelowy_test", email="model@testowy.pl")

    def test_authors_str(self):

        a1 = Author.objects.get(nick="modelowy_test")

        self.assertEqual(a1.nick, "modelowy_test")
        self.assertEqual(a1.email, "model@testowy.pl")

