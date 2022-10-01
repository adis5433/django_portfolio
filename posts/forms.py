from django import forms
from posts.models import Post, Author

class PostForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        title  = cleaned_data.get('title')
        content = cleaned_data.get('content')
        author = forms.ChoiceField(
            choices=((a.id, a.nick) for a in Author.objects.all())
        )
        tags = forms.ChoiceField(
            choices=((t.word) for t in Tags.objects.all())
        )

        if not title or content:
            raise forms.ValidationError("Należy podać wszystkie wartości")

    class Meta:
        model = Post
        fields = "__all__"
        fields = ["title", "content", "author", "image","tags"]

class PostSearcherForm(forms.Form):
    searched_title = forms.CharField(label="Szukaj", max_length = 30)


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



class EditPostForm(forms.ModelForm):



        def clean(self):
            cleaned_data = super().clean()
            title = cleaned_data.get('title')
            content = cleaned_data.get('content')
            tags = cleaned_data('tags')

        class Meta:
            model = Post
            fields = "__all__"
            fields = ["title", "content","tags"]
