from django.db import models
from shop.models import Product
from profiles.models import UserProfile


class ProductReview(models.Model):
    user = models.ForeignKey(UserProfile, related_name='user_reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_reviews', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    rating = models.PositiveIntegerField(default=1)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.title
