from django.db import models

class ProductModel(models.Model):
    
    product_name = models.CharField(max_length = 200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()


    def __str__(self):
        return self.product_name