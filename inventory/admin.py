from django.contrib import admin

from .models import Category, PropertyType, Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
admin.site.register(PropertyType)
