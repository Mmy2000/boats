from django.db import models
from django.utils import timezone
from django.utils.text import slugify 

# Create your models here.
class Services(models.Model):
    name = models.CharField( max_length=50)
    cover_image = models.ImageField(upload_to='services/' , default='')
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)
    category = models.ForeignKey('CategoryService',related_name='service_category',on_delete=models.CASCADE , default='')
    description = models.TextField(("description"),max_length=100000,null=True,blank=True)
    short_description = models.CharField( max_length=100)
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(Services,self).save(*args,**kwargs)

    class Meta:
        verbose_name = ("Services")
        verbose_name_plural = ("Services")

    def __str__(self):
        return self.name
    
class CategoryService(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True,blank=True , null=True, max_length=100)
    description = models.TextField( max_length=2000 , blank=True)
    image = models.ImageField( upload_to='cat_service_img' , blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(CategoryService,self).save(*args,**kwargs)

    def __str__(self):
        return self.name
    

class ServicesImages(models.Model):
    services = models.ForeignKey(Services,related_name='services_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='servicesimages/')

    class Meta:
        verbose_name = ("Services Images ")
        verbose_name_plural = ("Services Images ")

    def __str__(self):
        return str(self.services)