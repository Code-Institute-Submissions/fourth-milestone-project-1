from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    url = models.CharField(max_length=500, db_index=True)
    is_shown = models.BooleanField(default=False)

    def __str__(self):
        return self.name
