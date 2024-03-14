from django.db import models
from django.urls import reverse_lazy


class Car(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.brand} {self.model}"

    def get_absolute_url(self):
        return reverse_lazy("AppCar:detail", kwargs={"pk": self.pk})
