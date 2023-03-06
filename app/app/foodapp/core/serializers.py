from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
class Restaurant_TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_Table
        fields = '__all__'

class Catalog_Restaurant_TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog_Restaurant_Table
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
        
class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(read_only=True, many=True)
        
    class Meta:
        model = Recipe
        fields = '__all__'
        
class RestaurantSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(read_only=True, many=True)
    
    class Meta:
        model = Restaurant
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Reservation
        fields = '__all__'