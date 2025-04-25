from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    food = models.IntegerField(default=0)
    image = models.ImageField(upload_to='pet_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
