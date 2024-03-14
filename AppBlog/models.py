from django.db import models
from django.urls import reverse_lazy


class Blog(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse_lazy("AppBlog:detail", kwargs={"pk": self.pk})
