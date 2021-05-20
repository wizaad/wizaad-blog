from django.db import models
from django.urls import reverse


class Radio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    my_voice = models.URLField(max_length=2083)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={'pk': self.pk})
