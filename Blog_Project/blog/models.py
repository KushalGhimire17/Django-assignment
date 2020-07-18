from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=200)

    def __str__(self):
        return self.fullname

class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title