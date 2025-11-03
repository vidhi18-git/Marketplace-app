from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    file = models.FileField(upload_to='uploads')

    def __str__(self):
        return self.name
# Create Order model to store orders related data , like what are the orders made and placed        

class OrderDetail(models.Model):
    customer_email =models.EmailField()
    stripe_session_id = models.CharField(max_length=200, null=True, blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField()
    stripe_payment_intent = models.CharField(max_length=200,null=True,blank=True)
    has_paid = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
