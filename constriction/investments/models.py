from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseInvestment(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
