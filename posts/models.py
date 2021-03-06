from django.db import models
from django.db.models.base import Model

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(
        auto_now_add=False, auto_now=False, null=True, blank=True)
    
    def get_absolute_url(self):
        # return reverse("product:detail", kwargs={"pk": self.pk})
        return f'posts/{self.id}'

    @property
    def elastic_score(self):
        return 0.75
