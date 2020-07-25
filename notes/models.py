from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField('Название', max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Note(models.Model):
    name = models.CharField('Название', max_length=150, unique=True)
    description = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    publish = models.DateField(default=timezone.now())
    category = models.ManyToManyField(Category)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Записка"
        verbose_name_plural = "Записки"
        ordering = ('-publish',)
