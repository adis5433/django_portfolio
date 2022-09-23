from django import forms
from posts.models import Post, Author

class PostForm(forms.Form):
    title = forms.CharField(max_length=20)
    content = forms.CharField(max_length=1000,widget=forms.Textarea)
    author = forms.ChoiceField(choices=((a.id, a.nick) for a in Author.objects.all()))


    def clean(self):
        cleaned_data = super().clean()
        title  = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if not (title or content):
            raise forms.ValidationError("Należy podać wszystkie wartości")

class AuthorForm(forms.Form):
    nick = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=40)

    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('nick')
        email = cleaned_data.get('email')


        if not (nick or email):
            raise forms.ValidationError("Należy podać wszystkie wartości")