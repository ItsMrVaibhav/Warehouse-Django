from django.urls import path
from .views import index, viewProduct, editProduct, editLocation, viewLocation, editProductMovement, viewProductMovement, products, locations, productMovements, deleteProduct, deleteLocation, deleteProductMovement

app_name = "core"
urlpatterns = [
    path("", index, name = "index"),
    path("products/", products, name = "products"),
    path("locations/", locations, name = "locations"),
    path("product-movements/", productMovements, name = "productMovements"),
    path("view-product/<slug:productID>/", viewProduct, name = "viewProduct"),
    path("edit-product/<slug:productID>/", editProduct, name = "editProduct"),
    path("delete-product/<slug:productID>/", deleteProduct, name = "deleteProduct"),
    path("view-location/<slug:locationID>/", viewLocation, name = "viewLocation"),
    path("edit-location/<slug:locationID>/", editLocation, name = "editLocation"),
    path("delete-location/<slug:locationID>/", deleteLocation, name = "deleteLocation"),
    path("edit-product-movement/<slug:pMovementID>/", editProductMovement, name = "editProductMovement"),
    path("view-product-movement/<slug:pMovementID>/", viewProductMovement, name = "viewProductMovement"),
    path("delete-product-movement/<slug:pMovementID>/", deleteProductMovement, name = "deleteProductMovement"),
]