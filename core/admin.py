from django.contrib import admin
from .models import Location, Product, ProductMovement

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("product_id", "name", "dateCreated", "dateModified")

class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ("location_id", "name", "address", "pincode", "city", "state", "country", "dateCreated", "dateModified")

class ProductMovementAdmin(admin.ModelAdmin):
    model = ProductMovement
    list_display = ("movement_id", "getFromLocation", "getToLocation", "getProduct", "quantity", "dateCreated", "dateModified")

    def getFromLocation(self, movement):
        return movement.from_location.name if movement.from_location else ""

    getFromLocation.short_description = "From (Source)"

    def getToLocation(self, movement):
        return movement.to_location.name if movement.to_location else ""

    getToLocation.short_description = "To (Destination)"

    def getProduct(self, movement):
        return movement.product_id.name

    getProduct.short_description = "Product"

admin.site.register(Product, ProductAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(ProductMovement, ProductMovementAdmin)