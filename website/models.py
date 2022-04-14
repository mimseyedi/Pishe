from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f'{self.name} - {self.subject}'
