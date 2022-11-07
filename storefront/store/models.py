import email
from email.policy import default
from itertools import product
from operator import mod
from re import M
from secrets import choice
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Promotion(models.Model):
    descritpion = models.CharField(max_length=255)
    discount = models.FloatField()
    


class Collection(models.Model):
    title = models.CharField(max_length =255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null = True, related_name='+')

class Product(models.Model):
    title = models.CharField(max_length =255)
    description = models.TextField()
    price = models.DecimalField()
    #9999.99
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    inventory  = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey(Collection, on_delete = models.PROTECT)
    promotions = models.ManyToManyField(Promotion)
 
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_Glod = 'G' 

    MEMBERSHIP_CHOICES = [
        ('B','Bronze'),
        ('S','Silver'),
        ('G','Glod')
    ]
    first_name = models.CharField(max_length =255)
    last_name = models.CharField(max_length =255)
    email = models.EmailField(unique =True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null = True)
    membership = models.CharField(max_length = 1, choices = MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE)

class Order(models.Model):

    placed_at = models.DateTimeField(auto_now_add= True)
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS = [
        ('P','Pending'),
        ('C','Complete'),
        ('F','Failed')
    ]
    payment_status = models.CharField(max_length = 255,choices = PAYMENT_STATUS, default = PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE) 
    # item = models.ForeignKey(Item, on_delete = models.CASCADE)

class Address (models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length= 255)
    # customer = models.OneToOneField(Customer, on_delete= models.CASCADE, primary_key = True)  # one to one solution 
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE) 

class Cart(models.Model):
    title = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField() 

class OrderItem(models.Model):
    name = models.CharField(max_length= 255)
    order = models.ForeignKey(Order, on_delete = models.PROTECT) 
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2)
     


   


    

