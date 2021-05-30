from django.db import models
from django.db.models.deletion import CASCADE
from authentication.models import Uzer

# Create your models here.


class Chapter(models.Model):
    files = models.FileField(upload_to='files')


class Book(models.Model):
    title = models.CharField(max_length=250)
    cover = models.ImageField(upload_to='cover')
    author = models.ForeignKey(Uzer, on_delete=CASCADE)
    chapters = models.ManyToManyField(Chapter)
