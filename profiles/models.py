from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_address_line1 = models.CharField(max_length=100, blank=True)
    default_address_line2 = models.CharField(max_length=100, blank=True)
    default_town_or_city = models.CharField(max_length=40, blank=True)
    default_postcode = models.CharField(max_length=20, blank=True)
    default_country = CountryField(blank_label='Select a country', null=True,
                                   blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
