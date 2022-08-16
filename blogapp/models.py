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
    image_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return f"{self.title} by {self.author}"


