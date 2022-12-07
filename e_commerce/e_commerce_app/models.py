from django.db import models

# Create your models here.


class item(models.Model):
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField()
    item_img=models.ImageField(upload_to='media/')
    quantitie=models.CharField(max_length=30, default=None)
    brand_name=models.CharField(max_length=100, default=None)
    category=models.CharField(max_length=100, default=None)