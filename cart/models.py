from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField( max_length=50)
    product_price=models.IntegerField()
    pub_date=models.DateTimeField(auto_now=True)
    product_desc=models.CharField(max_length=300)
    product_image=models.ImageField(upload_to='shop/images',default="")
    def __str__(self):
        return self.product_name