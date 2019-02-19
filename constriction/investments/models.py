from autoslug import AutoSlugField
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


class Investment(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    price = models.IntegerField(null=True)
    url = models.URLField(null=True)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
