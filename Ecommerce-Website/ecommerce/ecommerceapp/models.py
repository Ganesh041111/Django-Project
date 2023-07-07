from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    desc=models.TextField(max_length=800)
    phonenumber=models.IntegerField()

    def __str__(self):
        return self.name
