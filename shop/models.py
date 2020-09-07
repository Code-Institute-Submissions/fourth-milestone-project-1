from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    friendly_name = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, related_name='products', on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    primary_image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(null=True, blank=True)
    customisable = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='product_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d')

    class Meta:
        ordering = ('product',)

    def __str__(self):
        return self.name
