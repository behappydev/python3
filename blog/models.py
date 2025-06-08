from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField("Nombre", max_length=100)
    bio  = models.TextField("Biografía", blank=True)

    def __str__(self): return self.name


class Category(models.Model):
    name = models.CharField("Categoría", max_length=50, unique=True)
    description = models.TextField("Descripción", blank=True)

    def __str__(self): return self.name


class Post(models.Model):
    title      = models.CharField("Título", max_length=200)
    content    = models.TextField("Contenido")
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    author     = models.ForeignKey(Author, on_delete=models.CASCADE)
    category   = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self): return self.title
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.pk])
