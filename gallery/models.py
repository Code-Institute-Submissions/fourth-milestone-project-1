from django.db import models


class GalleryImage(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='gallery/%Y/%m/%d', blank=False)
    is_shown = models.BooleanField(default=False)

    def __str__(self):
        return self.name
