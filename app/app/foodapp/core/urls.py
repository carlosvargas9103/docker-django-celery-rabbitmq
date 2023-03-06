# core/restaurant/urls.py
from django.contrib import admin
from django.urls import path, include

# import routers
from rest_framework import routers 
from .views import *

# import for the documentation with swagger
# https://hackernoon.com/openapi-30-schema-with-swagger-ui-for-django-restful-app-4w293zje
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
  
# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used from the .views file in the app
router.register(r'restaurants', RestaurantModelViewSet)
router.register(r'recipes', RecipeModelViewSet)
router.register(r'ingredients', IngredientModelViewSet)
router.register(r'restaurant-tables', Restaurant_TableModelViewSet)
router.register(r'customers', CustomerModelViewSet)
router.register(r'reservations', ReservationModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/",SpectacularSwaggerView.as_view(template_name="swagger-ui.html", url_name="schema"),name="swagger-ui",),    
]