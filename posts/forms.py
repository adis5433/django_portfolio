from django import forms
from posts.models import Post, Author

class PostForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        title  = cleaned_data.get('title')
        content = cleaned_data.get('content')
        author = clened_data.get('author')

        if not title or content:
            raise forms.ValidationError("Należy podać wszystkie wartości")

    class Meta:
        model = Post
        fields = ["title", "content", "author"]



class AuthorForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('nick')
        email = cleaned_data.get('email')


        if not (nick or email):
            raise forms.ValidationError("Należy podać wszystkie wartości")

    class Meta:
        model = Author
        fields = ["nick", "email"]
