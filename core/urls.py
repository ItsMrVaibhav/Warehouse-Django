from django.urls import path
from .views import index, viewProduct, editProduct, editLocation, viewLocation, editProductMovement, viewProductMovement, report, locationReport, products, locations, productMovements

app_name = "core"
urlpatterns = [
    path("", index, name = "index"),
    path("products/", products, name = "products"),
    path("locations/", locations, name = "locations"),
    path("product-movements/", productMovements, name = "productMovements"),
    path("view-product/", viewProduct, name = "viewProduct"),
    path("edit-product/", editProduct, name = "editProduct"),
    path("view-location/", viewLocation, name = "viewLocation"),
    path("edit-location/", editLocation, name = "editLocation"),
    path("edit-product-movement/", editProductMovement, name = "editProductMovement"),
    path("view-product-movement/", viewProductMovement, name = "viewProductMovement"),
    path("report/", report, name = "report"),
    path("location-report/", locationReport, name = "locationReport"),
]