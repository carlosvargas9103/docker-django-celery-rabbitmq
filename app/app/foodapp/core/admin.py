from django.contrib import admin
from .models import *

# Register your models here.

class Table2RestaurantInline(admin.TabularInline):
    model = Restaurant_Table
    extra = 1

class Reservation2ManyInline(admin.TabularInline):
    model = Reservation
    extra = 1

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','res_type')
    list_filter = ('res_type',)
    inlines = [
        Table2RestaurantInline,
    ]

admin.site.register(Restaurant, RestaurantAdmin)

class Restaurant_TableAdmin(admin.ModelAdmin):
    list_display = ('restaurant','number_table')
    list_filter = ('restaurant',)
    
admin.site.register(Restaurant_Table, Restaurant_TableAdmin)

class Catalog_Restaurant_TableAdmin(admin.ModelAdmin):
    list_display = ('table_restaurant','restaurant')
    list_filter = ('restaurant',)
    
#admin.site.register(Catalog_Restaurant_Table, Catalog_Restaurant_TableAdmin)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name','recipe_type')
    list_filter = ('recipe_type',)
    filter_horizontal = ('ingredients',)
    
#admin.site.register(Recipe, RecipeAdmin)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name','alergy')
    list_filter = ('alergy',)
    
#admin.site.register(Ingredient, IngredientAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    
admin.site.register(Customer, CustomerAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_code','table_restaurant','customer','date')
    list_filter = ('date', 'customer')
    
admin.site.register(Reservation, ReservationAdmin)