from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    shop_image = models.ImageField(upload_to='shop')

    def __str__(self):
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField(null=True)
    amount = models.IntegerField()
    product_image = models.ImageField(upload_to='product')
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.title}"





