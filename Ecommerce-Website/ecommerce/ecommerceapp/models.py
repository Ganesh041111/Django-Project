from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    desc=models.TextField(max_length=800)
    phonenumber=models.IntegerField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100, default="")
    subcategory=models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    image=models.ImageField(upload_to='image/image')

    def __str__(self):
        return self.product_name


