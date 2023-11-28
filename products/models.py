from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    slogan = RichTextUploadingField(null=True, blank=True, default=None)
    about_short = RichTextUploadingField(null=True, blank=True)
    about = RichTextUploadingField(null=True, blank=True)
    Vision = RichTextUploadingField(null=True, blank=True)
    Mission = RichTextUploadingField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=200)
    Category_image = models.ImageField(upload_to='productcategory/')

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=500)
    product_short = RichTextUploadingField(null=True, blank=True, default=None)
    product_description = RichTextUploadingField(null=True, blank=True)
    product_video = models.URLField()
    product_image = models.ImageField(null=True, blank=True, upload_to='products/')
    product_category = models.ForeignKey(ProductCategory,  on_delete=models.CASCADE, default=None)
    product_slug = models.SlugField(unique=True)

    def __str__(self):
        return self.product_name

class ProductMedia(models.Model):
    product_media = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='add_product_image')
    p_image = models.ImageField(upload_to='products/', null=True, blank=True)
    p_video = models.URLField(null=True, blank=True)

class Founder(models.Model):
    founder_name = models.CharField(max_length=200)
    founder_short_des = RichTextUploadingField(null=True, blank=True)
    founder_des = RichTextUploadingField()
    fname_slug = models.SlugField(unique=True, default=None, blank=True, null=True)

    def __str__(self):
        return self.founder_name

class Team(models.Model):
    team_member_name = models.CharField(max_length=100, default='name')
    team_member_img = models.ImageField(upload_to='team/') 
    team_member = models.CharField(max_length=200)
    team_member_short = RichTextUploadingField()
    team_member_des = RichTextUploadingField()
    tname_slug = models.SlugField(unique=True, default=None, blank=True, null=True)

    def __str__(self):
        return self.team_member



