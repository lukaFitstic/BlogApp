from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    stageName = models.CharField(max_length=50)
    def __str__(self):
        return self.stageName

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               default = None,
                               null = True)
    content = models.TextField()
    def __str__(self):
        return self.title