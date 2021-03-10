from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(
        auto_now_add=False, auto_now=False, null=True, blank=True)

    def get_absolute_url(self):
        # return reverse("product:detail", kwargs={"pk": self.pk})
        return f'products/{self.id}'

    @property
    def elastic_score(self):
        return 0.95
