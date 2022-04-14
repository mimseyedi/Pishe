from django.db import models


class PaperCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id} - {self.name}'


class PaperTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Paper(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    title = models.CharField(max_length=300)
    content = models.TextField()
    category = models.ManyToManyField(PaperCategory)
    tag = models.ManyToManyField(PaperTag)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(null=True, auto_now_add=True)
    updated_date = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.id} - {self.title}'
