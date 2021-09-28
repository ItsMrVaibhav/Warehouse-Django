from django.urls import path
from .views import index, addProduct, viewProduct, editProduct, addLocation, editLocation, viewLocation, addProductMovement, editProductMovement, viewProductMovement, report, locationReport, products, locations, productMovements

app_name = "core"
urlpatterns = [
    path("", index, name = "index"),
    path("products/", products, name = "products"),
    path("locations/", locations, name = "locations"),
    path("product-movements/", productMovements, name = "productMovements"),
    path("add-product/", addProduct, name = "addProduct"),
    path("view-product/", viewProduct, name = "viewProduct"),
    path("edit-product/", editProduct, name = "editProduct"),
    path("add-location/", addLocation, name = "addLocation"),
    path("view-location/", viewLocation, name = "viewLocation"),
    path("edit-location/", editLocation, name = "editLocation"),
    path("add-product-movement/", addProductMovement, name = "addProductMovement"),
    path("edit-product-movement/", editProductMovement, name = "editProductMovement"),
    path("view-product-movement/", viewProductMovement, name = "viewProductMovement"),
    path("report/", report, name = "report"),
    path("location-report/", locationReport, name = "locationReport"),
]