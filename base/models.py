from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class member(models.Model):

    username=models.CharField(max_length=50)
    passwd=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    position=models.CharField(max_length=50, default='Write Student / Teacher')

    def __str__(self):
        return self.username

class customer(models.Model):
    email= models.EmailField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
class product(models.Model):
    LENGTH=(
        ('45','45'),('60','60'),('90','90')
    )
    CATEGORY=(
        ('Full Course','Full Course'),('crash Course','crash Course')
    )
    TAGS=(
        ("Foreign","Foreign"),("Indian","Indian")
    )
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    host=models.CharField(max_length=200)
    description=models.TextField(max_length=200,null=True)
    experience=models.IntegerField(null=True)
    length=models.CharField(max_length=200,null=True,choices=LENGTH)
    timing_start=models.CharField(max_length=2,null=True)
    timing_end=models.CharField(max_length=2,null=True)
    tags=models.CharField(max_length=200,null=True,choices=TAGS)
    def __str__(self):
        return self.name

class order(models.Model):
    Customer=models.ForeignKey(customer,null=True,on_delete=models.SET_NULL)
    Product=models.ForeignKey(product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
    

