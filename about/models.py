from django.db import models

# Create your models here.
class About(models.Model):
    short_description = models.TextField(("short description"),max_length=1000)
    description = models.TextField(("description"),max_length=100000)
    image_cover = models.ImageField(upload_to='about/')

    class Meta:
        verbose_name = ("About CEO")
        verbose_name_plural = ("About CEO")

    def __str__(self):
        return str(self.id)