from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    tags = models.ManyToManyField("posts.Tag", related_name="posts")
    author = models.ForeignKey(
        'posts.Author',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return f"id:{self.id}, title={self.title}, author={self.author}, image={self.image}"

    class Meta:
        ordering = ["-id"]

class Author(models.Model):
    nick = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=40, unique=True)

    def __str__(self):
        return self.nick

class Tag(models.Model):
   word = models.CharField(max_length=50, unique=True)
   created = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.word