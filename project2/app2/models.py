from django.db import models

class RegistrationData(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50)


class UploadFetch(models.Model):
    iid=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    upload_img = models.ImageField(upload_to='images/')

class ProductData(models.Model):
    pid=models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_class = models.CharField(max_length=50)
    product_color = models.CharField(max_length=10)
    product_cost = models.IntegerField()
