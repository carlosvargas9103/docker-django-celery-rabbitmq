#core/restaurant/views.py
#from django.contrib.auth.models import User
from time import sleep

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
  
# import local data
from .serializers import *
from .models import *
from .tasks import *


#############
# Restaurant
class RestaurantModelViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    lookup_field = 'id'
    
    def get_queryset(self):
        return self.queryset

    def get_object(self):
        sku_id = self.kwargs['id']
        return get_object_or_404(Restaurant, pk=sku_id)

    def list(self, request):
        restaurants = Restaurant.objects.all()
        serializers = self.get_serializer(restaurants, many=True)
        return Response(serializers.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)
        return Response(serializers.data)

#########
# Recipe
class RecipeModelViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    lookup_field = 'id'
    
    def get_queryset(self):
        return self.queryset

    def get_object(self):
        sku_id = self.kwargs['id']
        return get_object_or_404(Recipe, pk=sku_id)

    def list(self, request):
        recipes = Recipe.objects.all()
        serializers = self.get_serializer(recipes, many=True)
        return Response(serializers.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)
        return Response(serializers.data)
    
##############    
# Ingredients
class IngredientModelViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    lookup_field = 'id'
    
    def get_queryset(self):
        return self.queryset

    def get_object(self):
        sku_id = self.kwargs['id']
        return get_object_or_404(Ingredient, pk=sku_id)

    def list(self, request):
        ingredients = Ingredient.objects.all()
        serializers = self.get_serializer(ingredients, many=True)
        return Response(serializers.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)
        return Response(serializers.data)
    
##################  
# Restaurant_Table
class Restaurant_TableModelViewSet(viewsets.ModelViewSet):
    serializer_class = Restaurant_TableSerializer
    queryset = Restaurant_Table.objects.all()
    lookup_field = 'id'
    
    def get_queryset(self):
        return self.queryset

    def get_object(self):
        sku_id = self.kwargs['id']
        return get_object_or_404(Restaurant_Table, pk=sku_id)

    def list(self, request):
        Restaurant_Tables = Restaurant_Table.objects.all()
        serializers = self.get_serializer(Restaurant_Tables, many=True)
        return Response(serializers.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)
        return Response(serializers.data)
    
##########################  
# Catalog_Restaurant_Table
class Catalog_Restaurant_TableModelViewSet(viewsets.ModelViewSet):
    serializer_class = Catalog_Restaurant_TableSerializer
    queryset = Catalog_Restaurant_Table.objects.all()
    lookup_field = 'id'
    
    def get_queryset(self):
        return self.queryset

    def get_object(self):
        sku_id = self.kwargs['id']
        return get_object_or_404(Catalog_Restaurant_Table, pk=sku_id)

    def list(self, request):
        Catalog_Restaurant_Tables = Catalog_Restaurant_Table.objects.all()
        serializers = self.get_serializer(Catalog_Restaurant_Tables, many=True)
        return Response(serializers.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)
        return Response(serializers.data)
    
##########  
# Customer
class CustomerModelViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'id'
    
    def get_queryset(self):
        return self.queryset

    def get_object(self):
        sku_id = self.kwargs['id']
        return get_object_or_404(Customer, pk=sku_id)

    def list(self, request):
        Customers = Customer.objects.all()
        serializers = self.get_serializer(Customers, many=True)
        return Response(serializers.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)
        return Response(serializers.data)

#############  
# Reservation
class ReservationModelViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    lookup_field = 'id'
    
    def get_queryset(self):
        return self.queryset

    def get_object(self):
        sku_id = self.kwargs['id']
        return get_object_or_404(Reservation, pk=sku_id)

    def list(self, request):
        Reservations = Reservation.objects.all()
        serializers = self.get_serializer(Reservations, many=True)
        return Response(serializers.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)
        return Response(serializers.data)
    
    def create(self, request, *args, **kwargs):
        # Retrieving attriubutes for Celery task
        date = request.data.get('date')
        customer = request.data.get('customer')
        table_restaurant = request.data.get('table_restaurant')
        # Calling Serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # Calling Celery task
        #for i in range(9999):
        send_email_reservation_async.delay(date)
        # Response to client thru API
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        #print(serializer)
        serializer.save()