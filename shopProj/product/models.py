import uuid
from logging import Manager
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class ProductManager(models.Manager):
    def buyable(self):
        return self.filter(is_active=True)
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Product(models.Model):
    # Use constants for choices
    class SizeChoices(models.TextChoices):
        EXTRA_SMALL = 'XS', 'Extra Small'
        SMALL = 'S', 'Small'
        MEDIUM = 'M', 'Medium'
        LARGE = 'L', 'Large'
        EXTRA_LARGE = 'XL', 'Extra Large'

    size = models.CharField(
        max_length=2,
        choices=SizeChoices.choices,
        default=SizeChoices.MEDIUM,
    )
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    is_active = models.BooleanField()
    image = models.ImageField(upload_to = 'product', blank=True)
    slug = models.SlugField(blank=True, unique=True)
    objects = models.Manager()
    objects_2 = ProductManager()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.description}"

    def get_absolute_url(self):
        return reverse('product:details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super(Product, self).save()

class Comment(models.Model):
    parent_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'body: {self.body[:30]}'
