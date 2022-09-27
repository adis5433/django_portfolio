from unittest import TestCase
from django.test import Client
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm
# Create your tests here.


class PostsFormTest(forms.ModelForm):

    def test_post_save_correct_data(self):
        data = {"value": 200}
        self.assertEqual(len(Post.objects.all()), 0)
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(p, Post)
        self.assertEqual(p.value, 200)
        self.assertIsNotNone(p.id)
        self.assertIsNone(p.error)

class PostsFormTest(forms.ModelForm):

    def test_post_save_correct_data(self):
        data = {"value": 200}
        self.assertEqual(len(Post.objects.all()), 0)
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(p, Post)
        self.assertEqual(p.value, 200)
        self.assertIsNotNone(p.id)
        self.assertIsNone(p.error)


class AuthorsFormTest(forms.ModelForm):

    def test_author_save_correct_data(self):
        data = {"value": 200}
        self.assertEqual(len(Post.objects.all()), 0)
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(a, Author)
        self.assertEqual(a.value, 200)
        self.assertIsNotNone(a.id)
        self.assertIsNone(a.error)