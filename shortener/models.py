from django.db import models

# Create your models here.
from django.db import models
import string
import random

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=15, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code()
        super().save(*args, **kwargs)

    def generate_short_code(self):
        length = 6
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))