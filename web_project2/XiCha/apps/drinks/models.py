from django.db import models

# # Create your models here.
# 点单页面列表模型
class Category(models.Model):
    name = models.CharField(null=False, max_length=50)
    sort = models.IntegerField()
    category_image_url = models.URLField(max_length=256, blank=True)
    gary_category_image_url = models.URLField(max_length=256, blank=True)

# 奶茶模型
class Product(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.TextField(max_length=500)
    intro = models.TextField(max_length=500)
    category_id = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    sort = models.IntegerField()
    image = models.URLField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Shop(models.Model):
    name = models.CharField(null=False, max_length=50)