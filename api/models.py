from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='',blank=True)
    website = models.CharField(max_length=100,default='https://www.google.com')

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    price = models.FloatField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} - {self.company.name}'
    
class Category(models.Model):
    name=models.CharField(max_length=30)
    products = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return self.name
    