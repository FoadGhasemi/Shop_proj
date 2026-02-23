from django.contrib.auth.models import User
from django.db import models
from django.templatetags.static import static
from product.models import Product

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    image = models.ImageField(null=True, blank=True, upload_to='profiles',
                              default= 'profiles/Untitled.jpg')

    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username