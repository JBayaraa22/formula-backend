from django.db import models

# Create your models here.


class Formula(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey("category" , on_delete=models.PROTECT, verbose_name="Ангилал")
    #audit
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now=True)


