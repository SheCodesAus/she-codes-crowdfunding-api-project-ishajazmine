from django.contrib.auth import get_user_model
from django.db import models

# categories - 
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

# Create your models here.
class   Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    # owner = models.CharField(max_length=200)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    categories = models.ManyToManyField(Category, null = True, blank = True)
    

# pledge model
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    # supporter = models.CharField(max_length=200)
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
