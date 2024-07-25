from django.db import models

# Create your models here.
class AboutUS(models.Model):
    short_description = models.TextField(("short description"),max_length=1000)
    description = models.TextField(("description"),max_length=100000)
    image_cover = models.ImageField(upload_to='about/')

    class Meta:
        verbose_name = ("About US")
        verbose_name_plural = ("About US")

    def __str__(self):
        return str(self.id)
    
class FAQ(models.Model):
    title = models.CharField( max_length=150)
    description = models.TextField(max_length=3000)

    def __str__(self):
        return self.title