from django.db import models

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    similar_categories = models.ManyToManyField('self', symmetrical=True, blank=True)

    def __str__(self):
        return self.name
