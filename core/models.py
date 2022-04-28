from django.db import models
from cloudinary.models import CloudinaryField
from django.forms import CharField
# Create your models here.

class Challenge(models.Model):
    page = CloudinaryField('image', blank=False)
    title = models.CharField(max_length=255,blank=False)
    description = models.CharField(max_length=1000,blank=False)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title