from django.db import models
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name()}"


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="blogapp")
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return f"{self.title} by {self.author}"


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=200)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")


