from django.db.models import Q
from django.shortcuts import render
from django.contrib import messages
from .models import Product, Location, ProductMovement
from django.http import HttpResponseRedirect, JsonResponse

def isValid(input):
    if input not in [None, ""]:
        if isinstance(input, int) or isinstance(input, float):
            return input >= 0

        return True

    return False

def getProduct(productID):
    """
    If the product exists, it returns the product, otherwise, None
    """
    product = Product.objects.filter(pk = productID)

    if not product.exists():
        return None

    product = product.first()
    return product

def getLocation(locationID):
    """
    If the location exists, it returns the location, otherwise, None
    """
    location = Location.objects.filter(pk = locationID)

    if not location.exists():
        return None

    location = location.first()
    return location

def index(request):
    """
    A view to home page
    """
    data = getAllLocationsProducts()
    data = {key: value for key, value in sorted(data.items(), key = lambda item: len(item[1]["products"]), reverse = True)}
    return render(request, "core/index.html", {
        "data": data
    })

def getAllLocationsProducts():
    """
    A function to get products data of all the locations
    """
    locations = Location.objects.all()
    data = {}

    for location in locations:
        data[location.pk] = {
            "location": location,
            "products": getLocationProducts(location)
        }

    return data

def getLocationProducts(location):
    """
    A function to get products data of a location
    """
    movements = ProductMovement.objects.filter(
        Q(from_location = location) |
        Q(to_location = location)
    )
    data = {}

    for movement in movements:
        if movement.from_location == None or movement.to_location == location:
            if not movement.product_id.pk in data.keys():
                data[movement.product_id.pk] = {
                    "quantity": 0,
                    "name": movement.product_id.name,
                    "id": movement.product_id.pk  
                }

            data[movement.product_id.pk]["quantity"] += movement.quantity
        elif movement.to_location == None or movement.from_location == location:
            if not movement.product_id.pk in data.keys():
                data[movement.product_id.pk] = {
                    "quantity": 0,
                    "name": movement.product_id.name,
                    "id": movement.product_id.pk
                }

            data[movement.product_id.pk]["quantity"] -= movement.quantity

    return data

def products(request):
    """
    A view to view all existing products
    """
    if request.method == "POST":
        # Fetching form data
        productID = request.POST.get("productID", "").strip()
        productName = request.POST.get("productName", "").strip()
        description = request.POST.get("productDescription", "").strip()
        values = {}
        error = False

        # Validating form data
        if productID is None or not isValid(productName):
            messages.error(request, "Invalid product ID")
            error = True
        else:
            values["productID"] = productID

        if productName is None or not isValid(productName):
            messages.error(request, "Invalid product name")
            error = True
        else:
            values["productName"] = productName

        if description is None or not isValid(description):
            messages.error(request, "Invalid product description")
            error = True
        else:
            values["description"] = description

        if Product.objects.filter(pk = productID).exists():
            messages.error(request, "Product ID aleardy exists! Enter a new product ID!")
            error = True

        if error:
            products, movements = getProductsAndMovements()
            return render(request, "core/products.html", {
                "products": zip(products, movements),
                "values": values
            })

        Product.objects.create(
            product_id = productID,
            name = productName,
            description = description
        )
        messages.success(request, "Product added successfully!")
        return HttpResponseRedirect(f"/view-product/{productID}")
    
    products, movements = getProductsAndMovements()
    return render(request, "core/products.html", {
        "products": zip(products, movements),
    })

def getProductsAndMovements():
    products = Product.objects.all()
    movements = []

    for product in products:
        movements.append(product.movements.all().count())

    return products, movements

def getLocationsData():
    """
    A function to get information about all the locations
    """
    locations = Location.objects.all()
    metrics = []

    for location in locations:
        metrics.append({
            "sources": location.sources.all().count(),
            "destinations": location.destinations.all().count()
        })

    return locations, metrics

def locations(request):
    """
    A view to view all existing locations
    """
    if request.method == "POST":
        # Fetching form data
        locationID = request.POST.get("locationID", "").strip()
        locationName = request.POST.get("locationName", "").strip()
        address = request.POST.get("address", "").strip()
        pincode = request.POST.get("pincode", "").strip()
        city = request.POST.get("city", "").strip()
        state = request.POST.get("state", "").strip()
        country = request.POST.get("country", "").strip()
        values = {}
        error = False

        # Validating form data
        if locationID is None or not isValid(locationID):
            messages.error(request, "Invalid location ID")
            error = True
        else:
            values["locationID"] = locationID

        if locationName is None or not isValid(locationName):
            messages.error(request, "Invalid location name")
            error = True
        else:
            values["locationName"] = locationName

        if address is None or not isValid(address):
            messages.error(request, "Invalid address")
            error = True
        else:
            values["address"] = address

        if pincode is None or not isValid(pincode):
            messages.error(request, "Invalid pincode")
            error = True
        else:
            values["pincode"] = pincode

        if city is None or not isValid(city):
            messages.error(request, "Invalid city")
            error = True
        else:
            values["city"] = city

        if state is None or not isValid(state):
            messages.error(request, "Invalid state")
            error = True
        else:
            values["state"] = state

        if country is None or not isValid(country):
            messages.error(request, "Invalid country")
            error = True
        else:
            values["country"] = country

        if Location.objects.filter(pk = locationID).exists():
            messages.error(request, "Location ID aleardy exists! Enter a new location ID!")
            error = True

        if error:
            locations, metrics = getLocationsData()
            return render(request, "core/locations.html", {
                "locations": zip(locations, metrics),
                "values": values
            })

        Location.objects.create(
            location_id = locationID,
            name = locationName,
            address = address,
            pincode = pincode,
            city = city,
            state = state,
            country = country
        )
        messages.success(request, "Location added successfully!")
        return HttpResponseRedirect(f"/view-location/{locationID}")

    locations, metrics = getLocationsData()
    return render(request, "core/locations.html", {
        "locations": zip(locations, metrics)
    })

def productMovements(request):
    """
    A view to view all existing product movements
    """
    if request.method == "POST":
        # Fetching form data
        movementID = request.POST.get("movementID", None).strip()
        fromLocation = request.POST.get("fromLocation", None).strip()
        toLocation = request.POST.get("toLocation", None).strip()
        product = request.POST.get("product", None).strip()
        quantity = int(request.POST.get("quantity", -1))
        values = {}
        error = False

        # Validating form data
        if movementID is None or not isValid(movementID):
            messages.error(request, "Invalid movement ID")
            error = True
        else:
            values["movementID"] = movementID

        if (fromLocation in [None, "none", ""] and toLocation in [None, "none", ""]) or (fromLocation == toLocation):
            messages.error(request, "Both the locations can't be none/same")
            error = True

        if product is None or not isValid(product):
            messages.error(request, "Invalid product")
            error = True
        else:
            values["product"] = product

        if quantity is None or not isValid(quantity):
            messages.error(request, "Invalid quantity")
            error = True
        else:
            values["quantity"] = quantity

        if not Product.objects.filter(pk = product).exists():
            messages.error(request, "Product doesn't exist!")
            error = True

        if fromLocation != "none" and not Location.objects.filter(pk = fromLocation).exists():
            messages.error(request, "From location doesn't exist!")
            error = True
        
        if toLocation != "none" and not Location.objects.filter(pk = toLocation).exists():
            messages.error(request, "To location doesn't exist!")
            error = True

        product = Product.objects.get(pk = product)

        # Checking if the quantity being transferred or moved out doesn't exceed the available amount
        if (toLocation == "none" and fromLocation != "none") or (toLocation != "none" and fromLocation != "none"):
            location = Location.objects.get(pk = fromLocation)
            data = getLocationProducts(location)

            if product.pk in data.keys():
                if quantity > data[product.pk]["quantity"]:
                    messages.error(request, "Quantity should not be more that the available units")
                    error = True
            else:
                messages.error(request, "No such product exists in the selected from location")
                error = True

        if ProductMovement.objects.filter(pk = movementID).exists():
            messages.error(request, "Movement ID already exists! Enter a new movement ID.")
            error = True

        if error:
            return render(request, "core/product-movements.html", {
                "productMovements": ProductMovement.objects.all(),
                "locations": Location.objects.all(),
                "products": Product.objects.all(),
                "values": values,
                "data": getAllLocationsProducts()
            })

        ProductMovement.objects.create(
            movement_id = movementID,
            from_location = None if fromLocation == "none" else Location.objects.get(pk = fromLocation),
            to_location = None if toLocation == "none" else  Location.objects.get(pk = toLocation),
            product_id = product,
            quantity = quantity,
            type = getProductMovementType(toLocation, fromLocation)
        )
        messages.success(request, "Product Movement added successfully!")
        return HttpResponseRedirect(f"/view-product-movement/{movementID}")

    return render(request, "core/product-movements.html", {
        "productMovements": ProductMovement.objects.all(),
        "locations": Location.objects.all(),
        "products": Product.objects.all(),
        "data": getAllLocationsProducts()
    })

def getProductMovementType(toLocation, fromLocation):
    if toLocation == "none" and fromLocation != "none":
        return "MO"
    elif toLocation != "none" and fromLocation == "none":
        return "MI"
    elif toLocation != "none" and fromLocation != "none":
        return "TR"

def viewProduct(request, productID):
    """
    A view to view an existing product
    """
    product = getProduct(productID)

    if not product:
        messages.error(request, "Product doesn't exist!")
        return HttpResponseRedirect("/")

    return render(request, "core/view-product.html", {
        "product": product,
        "movement": product.movements.all().count()
    })

def editProduct(request, productID):
    """
    A view to edit an existing product
    """
    product = getProduct(productID)

    if not product:
        messages.error(request, "Product doesn't exist!")
        return HttpResponseRedirect("/products/")

    if request.method == "POST":
        # Fetching form data
        productName = request.POST.get("productName", "").strip()
        description = request.POST.get("productDescription", "").strip()
        error = False

        # Validating form data
        if productName is None or not isValid(productName):
            messages.error(request, "Invalid product name")
            error = True

        if description is None or not isValid(description):
            messages.error(request, "Invalid product description")
            error = True

        if not error:
            product.name = productName
            product.description = description
            product.save()
            messages.success(request, "Product updated successfully!")
    
    return render(request, "core/edit-product.html", {
        "product": product
    })

def deleteProduct(request, productID):
    if request.method == "POST":
        product = Product.objects.filter(pk = productID)

        if product.exists():
            messages.success(request, "Product deleted successfully!")
            product.first().delete()
        else:
            messages.error(request, "Product doesn't exist")

    return HttpResponseRedirect("/products/")

def editLocation(request, locationID):
    """
    A view to edit an existing location
    """
    location = getLocation(locationID)

    if not location:
        messages.error(request, "Location doesn't exist!")
        return HttpResponseRedirect("/locations/")

    if request.method == "POST":
        # Fetching form data
        name = request.POST.get("locationName", "").strip()
        address = request.POST.get("address", "").strip()
        pincode = request.POST.get("pincode", "").strip()
        city = request.POST.get("city", "").strip()
        state = request.POST.get("state", "").strip()
        country = request.POST.get("country", "").strip()
        error = False

        # Validating form data
        if name is None or not isValid(name):
            messages.error(request, "Invalid location name")
            error = True

        if address is None or not isValid(address):
            messages.error(request, "Invalid address")
            error = True

        if pincode is None or not isValid(pincode):
            messages.error(request, "Invalid pincode")
            error = True

        if city is None or not isValid(city):
            messages.error(request, "Invalid city")
            error = True

        if state is None or not isValid(state):
            messages.error(request, "Invalid state")
            error = True

        if country is None or not isValid(country):
            messages.error(request, "Invalid country")
            error = True

        # Updating and saving location
        if not error:
            location.name = name
            location.address = address
            location.pincode = pincode
            location.city = city
            location.state = state
            location.country = country
            location.save()
            messages.success(request, "Location updated successfully!")
    
    return render(request, "core/edit-location.html", {
        "location": location
    })

def viewLocation(request, locationID):
    """
    A view to view a existing location
    """
    location = getLocation(locationID)

    if not location:
        messages.error(request, "Location doesn't exist!")
        return HttpResponseRedirect("/locations/")
    
    return render(request, "core/view-location.html", {
        "location": location,
        "metrics": {
            "sources": location.sources.all().count(),
            "destinations": location.destinations.all().count()
        }
    })

def deleteLocation(request, locationID):
    if request.method == "POST":
        location = Location.objects.filter(pk = locationID)

        if location.exists():
            messages.success(request, "Location deleted successfully!")
            location.first().delete()
        else:
            messages.error(request, "Location doesn't exist")

    return HttpResponseRedirect("/locations/")

def editProductMovement(request, pMovementID):
    """
    A view to edit an existing product movement
    """
    movement = ProductMovement.objects.filter(pk = pMovementID)

    if not movement.exists():
        messages.error(request, "Location doesn't exist!")
        return HttpResponseRedirect("/locations/")
    
    movement = movement.first()

    if request.method == "POST":
        # Fetching form data
        fromLocation = request.POST.get("fromLocation", None).strip()
        toLocation = request.POST.get("toLocation", None).strip()
        product = request.POST.get("product", None).strip()
        quantity = int(request.POST.get("quantity", -1))
        error = False

        # Validating form data
        if (fromLocation in [None, "none", ""] and toLocation in [None, "none", ""]) or (fromLocation == toLocation):
            messages.error(request, "Both the locations can't be none/same")
            error = True

        if product is None or not isValid(product):
            messages.error(request, "Invalid product")
            error = True

        if quantity is None or not isValid(quantity):
            messages.error(request, "Invalid quantity")
            error = True

        if not Product.objects.filter(pk = product).exists():
            messages.error(request, "Product doesn't exist!")
            error = True

        if fromLocation != "none" and not Location.objects.filter(pk = fromLocation).exists():
            messages.error(request, "From location doesn't exist!")
            error = True
        
        if toLocation != "none" and not Location.objects.filter(pk = toLocation).exists():
            messages.error(request, "To location doesn't exist!")
            error = True

        product = Product.objects.get(pk = product)

        # Checking if the quantity being transferred or moved out doesn't exceed the available amount
        if (toLocation == "none" and fromLocation != "none") or (toLocation != "none" and fromLocation != "none"):
            location = Location.objects.get(pk = fromLocation)
            data = getLocationProducts(location)

            if product.pk in data.keys():
                if product == movement.product_id:
                    if quantity > (data[product.pk]["quantity"] + movement.quantity):
                        messages.error(request, "Quantity should not be more that the available units")
                        error = True
                else:
                    if quantity > data[product.pk]["quantity"]:
                        messages.error(request, "Quantity should not be more that the available units")
                        error = True
            else:
                messages.error(request, "No such product exists in the selected from location")
                error = True

        if not error:
            movement.from_location = None if fromLocation == "none" else Location.objects.get(pk = fromLocation)
            movement.to_location = None if toLocation == "none" else  Location.objects.get(pk = toLocation)
            movement.product_id = product
            movement.quantity = quantity
            movement.type = getProductMovementType(toLocation, fromLocation)
            messages.success(request, "Product Movement updated successfully!")
            movement.save()

    return render(request, "core/edit-product-movement.html", {
        "movement": movement,
        "toLocation": movement.to_location.pk if movement.to_location else "none",
        "fromLocation": movement.from_location.pk if movement.from_location else "none",
        "product": movement.product_id.pk,
        "locations": Location.objects.all(),
        "products": Product.objects.all(),
        "data": getAllLocationsProducts()
    })

def viewProductMovement(request, pMovementID):
    """
    A view to view an existing product movement
    """
    movement = ProductMovement.objects.filter(pk = pMovementID)

    if not movement.exists():
        messages.error(request, "Location doesn't exist!")
        return HttpResponseRedirect("/locations/")
    
    movement = movement.first()
    return render(request, "core/view-product-movement.html", {
        "movement": movement,
    })

def deleteProductMovement(request, pMovementID):
    if request.method == "POST":
        movement = ProductMovement.objects.filter(pk = pMovementID)

        if movement.exists():
            messages.success(request, "Product Movement deleted successfully!")
            movement.first().delete()
        else:
            messages.error(request, "Product Movement doesn't exist")

    return HttpResponseRedirect("/product-movements/")