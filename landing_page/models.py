from django.db import models
from optimized_image.fields import OptimizedImageField


class Picture(models.Model):
    name = models.CharField(max_length=200)
    image = OptimizedImageField(default='1.jpg')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
