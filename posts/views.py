from django.shortcuts import render
from posts.models import Post, Author
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from posts.forms import PostForm, AuthorForm, PostSearcherForm
# Create your views here.



def posts_list(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)
        print(form)
        if  form.is_valid():
            print("zwalidowany")
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Dodano nowy Post!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )
    elif request.method == "GET":
        search_form = PostSearcherForm(data=request.GET)
        if search_form.is_valid():
            title = search_form.cleaned_data["searched_title"]
            searched_posts = Post.objects.filter(title=title)
            searcher = PostSearcherForm()
            return render(
                request=request,
                template_name="posts/post_search_result.html",
                context={
                    "posts": searched_posts,
                    "search_form": search_form,
                    "searched_title": title
                }
            )

    searcher = PostSearcherForm()
    form = PostForm()
    posts = Post.objects.all()
    authors = Author.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="posts/post_list.html",
        context={
            "paginator": paginator,
            "posts": posts,
            "form": form,
            "search_form":searcher,
            "authors": authors
        }
    )


def single_post(request, id):
   post = Post.objects.get(id=id)
   author = Author.objects.get(id=post.author_id)
   return render(
       request=request,
       template_name="posts/single_post.html",
       context={"post": post, "author": author}
   )
@login_required
def authors_list(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        print(form.data)

        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Dodano nowy Post!!"
                )

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