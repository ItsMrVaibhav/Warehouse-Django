from django.contrib import admin
from .models import Location, Product, ProductMovement

admin.site.register(Location)
admin.site.register(Product)
admin.site.register(ProductMovement)