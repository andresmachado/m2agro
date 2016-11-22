from django.contrib import admin
from .models import Product, Harvest, Service


# Register your models here.

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0 

@admin.register(Harvest)
class HarvestAdmin(admin.ModelAdmin):
    list_display = ['name', 'initial_date', 'end_date']
    inlines = [ServiceInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'initial_date', 'end_date', 'total_cost']
    inlines = [ProductInline]
