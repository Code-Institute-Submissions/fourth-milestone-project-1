from django.db import models
from shop.models import Product
from profiles.models import UserProfile


class ProductReview(models.Model):
    user = models.ForeignKey(UserProfile, related_name='user_reviews', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_reviews', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    RATING_CHOICES = [
        (0, '0 Stars'),
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    rating = models.PositiveIntegerField(default=1, choices=RATING_CHOICES)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.title
