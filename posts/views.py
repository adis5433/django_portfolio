from django.shortcuts import render
from posts.models import Post, Author
from django.contrib import messages

from posts.forms import PostForm, AuthorForm
# Create your views here.
def posts_list(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)

        if  form.is_valid():
            author = Author.objects.get(pk=int(form.cleaned_data['author']))
            data = form.cleaned_data.copy()
            data['author'] = author
            print(data)
            Post.objects.create(**data)
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = PostForm()
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/post_list.html",
        context={
            "posts": posts,
            "form": form
        }
    )

    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/post_list.html",
        context={"posts": posts}
        )

def single_post(request, id):
   post = Post.objects.get(id=id)
   author = Author.objects.get(id=post.author_id)
   return render(
       request=request,
       template_name="posts/single_post.html",
       context={"post": post, "author": author}
   )

def authors_list(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        print(form.data)

        if form.is_valid():
            Author.objects.create(**form.cleaned_data)

    authors = Author.objects.all()
    form = AuthorForm()
    return render(
        request=request,
        template_name="posts/author_list.html",
        context = {
            "authors": authors,
            "form": form,
                   }

    )

def single_author(request, id):
    author = Author.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/single_author.html",
        context = {"author": author}
    )