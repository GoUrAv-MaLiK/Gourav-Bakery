from django.db import models



# Create your models here.
class Shipping_detail(models.Model):
   name=models.CharField(default=" ",max_length=100)
   address=models.CharField(default=" ", max_length=300)
   email=models.CharField( default=" ",max_length=200)
   state=models.CharField( default=" ",max_length=50)
   mobile_number=models.CharField(default=" ", max_length=15)
   zip=models.IntegerField()
   order_id=models.AutoField(primary_key=True)
   item_Json=models.CharField(default=" ", max_length=5000)
   # amount=models.IntegerField(default="0")





