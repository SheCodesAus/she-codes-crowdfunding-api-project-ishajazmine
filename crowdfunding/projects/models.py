from django.contrib.auth import get_user_model
from django.db import models
# from users.models import Category, CustomUser

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
    # date_created = models.DateTimeField()
    date_created = models.DateTimeField(auto_now=True, blank=True)
    # owner = models.CharField(max_length=200)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    # categories = models.ManyToManyField(Category, null = True, blank = True)
    # ^error message 'null has no effect on many to many field
    categories = models.ManyToManyField(Category, blank = True)
    

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

# user to user payments - not part of general pledge model 
class OneOffPayment(models.Model):
    amount = models.IntegerField()
    is_active = models.BooleanField()
    description = models.CharField(max_length= 200)