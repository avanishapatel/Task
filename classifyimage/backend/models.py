from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """
    User model.
    Add gender and phone number field in inbuilt user model.
    """
    gender = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'


class Category(models.Model):
    """
    Category model.
    """
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'categories'


class Tag(models.Model):
    """
    Tag model.
    """
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        db_table = 'tags'


class Image(models.Model):
    """
    Image model.
    """
    tag = models.ManyToManyField(Tag, through='ImageTag')
    image_url = models.CharField(max_length=100)
    image_name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    description = models.TextField()
    altertext = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.image_name

    class Meta:
        db_table = 'images'


class ImageTag(models.Model):
    """
    ImageTag model to get image and tag information.
    """
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True)
    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE)
    image = models.ForeignKey(to=Image, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images_tag'

