from django.db import models
from profiles.models import UserProfile


class Recipe(models.Model):
    user = models.ForeignKey(UserProfile, related_name='user_recipe', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='recipes/%Y/%m/%d', blank=True)
    score = models.PositiveIntegerField(default=0)
    ingredients = models.TextField(blank=False)
    instructions = models.TextField(blank=False)
    is_showcased = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title