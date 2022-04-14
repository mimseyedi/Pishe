from django.db import models
from django.contrib.auth.models import User


class BlogCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id} - {self.name}'


class BlogTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    title = models.CharField(max_length=300)
    content = models.TextField()
    category = models.ManyToManyField(BlogCategory)
    tag = models.ManyToManyField(BlogTag)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(null=True, auto_now_add=True)
    updated_date = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.id} - {self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.id} - {self.name}'

