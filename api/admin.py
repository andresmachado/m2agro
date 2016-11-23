from django.contrib import admin
from .models import Product, Harvest, Service, ProductServiceRelationship


# Register your models here.

class ProductInline(admin.TabularInline):
    model = ProductServiceRelationship
    extra = 0


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0 


@admin.register(Harvest)
class HarvestAdmin(admin.ModelAdmin):
    list_display = ['name', 'initial_date', 'end_date']
    inlines = [ServiceInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit', 'price']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'initial_date', 'end_date', 'total_cost']
    inlines = [ProductInline]
