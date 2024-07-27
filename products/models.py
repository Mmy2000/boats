from django.db import models
from django.utils import timezone
from django.utils.text import slugify 

# Create your models here.

class Product(models.Model):
    name = models.CharField(unique=True, max_length=50)
    image = models.ImageField(upload_to='product/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField( default=timezone.now)
    slug = models.SlugField(null=True,blank=True , unique=True)
    views = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey("Category", verbose_name=("category product"),related_name="product_category", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class ProductGallary(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE , default=None)
    image = models.ImageField( upload_to="product_gallary", max_length=255)

    class Meta:
        verbose_name_plural = "Product Gallary"

    def __str__(self):
        return str(self.product.name)