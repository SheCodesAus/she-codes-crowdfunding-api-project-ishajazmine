# from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# CATEGORY MODEL 
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

# Individual User Model
class CustomUser(AbstractUser):
    birth_name = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    bio = models.TextField(default = "", null = True, blank = True)
    pass
    def __str__(self):
        return self.username


# user group model
