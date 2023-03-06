from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
import uuid

# Create your models below:

RESTAURANT_TYPES = (
            # Restaurant can be from specific types such as:
            ('Vegi','Vegetarian'),
            ('Vegn','Vegan'),
            ('Pesc','Pescetarian'),
            ('Hlal','Halal'),
            ('Kosh','Kosher'),
            ('Gltf','Gluten-Free'),
            ('Stnd','Standard'),
            )

INGREDIENTS_UNITS = (
            # Mass 
            ('mg','milligram'),
            ('g','gram'),
            ('kg','kilogram'),
            ('lb','pound'),
            ('oz','ounce'),
            # Volume
            ('tsp','teaspoon'),
            ('tbs','tablespoon'),
            ('cup','cup'),
            ('pt','pint'),
            ('ml','milliliter'),
            ('l','liter'),
            ('dl','deciliter'),
            # Unit
            ('uni','Unit'),
            )

INGREDIENTS_AlLERGIES = (
            # Explained by its own description
            ('A','Cereals containing gluten'),
            ('B','Crustaceans'),
            ('C','Eggs'),
            ('D','Fish'),
            ('E','Peanuts'),
            ('F','Soja'),
            ('G','Milk and/or lactose'),
            ('H','Nuts'),
            ('N','No'),
            )

RECIPE_TYPE = (
            # Each @Recipe can be a Drink or a Food type
            ('F','Food'),
            ('D','Drink'),
            )

 
class Ingredient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='',blank=True, null=True)
    alergy = models.CharField(choices=INGREDIENTS_AlLERGIES,max_length=1,default='N', help_text='Allergy code')
    quantity = models.FloatField(default=1)
    units = models.CharField(choices=INGREDIENTS_UNITS,max_length=3,default='uni', help_text='Measurement unit')
    
    #Relationships
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['created']
        
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'quantity', 'units'], name='name_quantity_units')
        ]
          
class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='',blank=True, null=True)
    recipe_type = models.CharField(choices=RECIPE_TYPE, max_length=1,default='F', help_text='Food or drink?')
    ingredients = models.ManyToManyField('Ingredient',related_name='ingredients', blank=True)
    restaurant_recipe = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name="restaurant_recipe", blank=True, null=True)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['created']
class Restaurant_Table(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    number_table = models.CharField(max_length=9, default='')
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name="restaurant_table", blank=True, null=True)
    
    def __str__(self):
        return '{}_{}'.format(self.restaurant, self.number_table)
    class Meta:
        ordering = ['created']
        
        constraints = [
            models.UniqueConstraint(
                fields=['restaurant', 'number_table'], name='restaurant_table_code')
        ]

class Catalog_Restaurant_Table(models.Model):
    catalog_serial = models.CharField(max_length=1, default='',blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name="restaurant_restaurant_table")
    table_restaurant = models.ForeignKey('Restaurant_Table', on_delete=models.CASCADE, related_name="table_restaurant_table")
    
    def __str__(self):
        return self.catalog_serial
    class Meta:
        ordering = ['created']
        
        constraints = [
            models.UniqueConstraint(
                fields=['restaurant', 'table_restaurant'], name='catalog_restaurant_table')
        ]

class Restaurant(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=1000, default='', blank=True, null=True)
    res_type = models.CharField(choices=RESTAURANT_TYPES, max_length=4, default='Stnd', help_text='Restaurant type')
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']
        
class Customer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='', blank=True, null=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['created']
        
class Reservation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    reservation_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date = models.DateField(default=datetime.date.today)
    table_restaurant = models.ForeignKey('Restaurant_Table', on_delete=models.CASCADE, related_name="reservation_table")#, null=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name="reservation_customer")#, blank=True, null=True)
    
    def __str__(self):
        return '{}'.format(self.reservation_code)
    
    class Meta:
        ordering = ['created']
        
        constraints = [
            models.UniqueConstraint(fields=['table_restaurant', 'date'], name='table_restaurant_date')
        ]