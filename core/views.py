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
    product = Product.object.filter(pk = productID)

    if not product.exists():
        return None

    product = product.first()
    return product

def getLocation(locationID):
    """
    If the location exists, it returns the location, otherwise, None
    """
    location = Location.object.filter(pk = locationID)

    if not location.exists():
        return None

    location = location.first()
    return location

def index(request):
    """
    A view to home
    """
    return render(request, "core/index.html", {})

def products(request):
    """
    A view to view all existing products
    """
    if request.method == "POST":
        # Fetching form data
        productID = request.POST.get("productID", "").strip()
        productName = request.POST.get("productName", "").strip()
        productQuantity = int(request.POST.get("productQuantity", -1))
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

        if productQuantity is None or not isValid(productQuantity):
            messages.error(request, "Invalid product quantity")
            error = True
        else:
            values["productQuantity"] = productQuantity

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
            quantity = productQuantity,
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
        productID = request.POST.get("productID", "").strip()
        productName = request.POST.get("productName", "").strip()
        productQuantity = int(request.POST.get("productQuantity", -1))
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

        if productQuantity is None or not isValid(productQuantity):
            messages.error(request, "Invalid product quantity")
            error = True
        else:
            values["productQuantity"] = productQuantity

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
            quantity = productQuantity,
            description = description
        )
        messages.success(request, "Product added successfully!")
        return HttpResponseRedirect(f"/view-product/{productID}")

    locations, metrics = getLocationsData()
    return render(request, "core/locations.html", {
        "locations": zip(locations, metrics)
    })

def productMovements(request):
    """
    A view to view all existing product movements
    """
    return render(request, "core/product-movements.html", {
        "productMovements": ProductMovement.objects.all(),
        "locations": Location.objects.all(),
        "products": Product.objects.all()
    })

def viewProduct(request, productID):
    """
    A view to view an existing product
    """
    product = getProduct(productID)

    if not product:
        messages.error(request, "Product doesn't exist!")
        return HttpResponseRedirect("/")

    pass   

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
        productName = request.POST.get("productName", None)
        productQuantity = request.POST.get("productQuantity", None)
        product.name = productName,
        product.quantity = productQuantity
        product.save()
        messages.success(request, "Product updated successfully!")
    pass

def addLocation(request):
    """
    A view to add a new location
    """
    if request.method == "POST":
        # Fetching form data
        address = request.POST.get("address")
        pincode = request.POST.get("pincode")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        location = Location.objects.create(
            address = address,
            pincode = pincode,
            city = city,
            state = state,
            country = country
        )
        messages.success(request, "Location added successfully!")
        return HttpResponseRedirect(f"/view-location/{location.pk}")

    return HttpResponseRedirect("/locations/")

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
        address = request.POST.get("address")
        pincode = request.POST.get("pincode")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")

        # Updating and saving location
        location.address = address
        location.pincode = pincode
        location.city = city
        location.state = state
        location.country = country
        location.save()
        messages.success(request, "Location added successfully!")
    pass

def viewLocation(request, locationID):
    """
    A view to view a existing location
    """
    location = getLocation(locationID)

    if not location:
        messages.error(request, "Location doesn't exist!")
        return HttpResponseRedirect("/locations/")
    pass

def addProductMovement(request):
    """
    A view to add a new product movement
    """
    if request.method == "POST":
        # Fetching form data
        # movementID = request.POST.get("movementID")
        fromLocationID = request.POST.get("fromLocationID")
        toLocationID = request.POST.get("toLocationID")
        productID = request.POST.get("productID")
        quantity = request.POST.get("quantity")

        # Checks
        if not fromLocationID and not toLocationID:
            messages.error(request, "Atleast one location is needed.")
            return HttpResponseRedirect("/product-movements/")

        # Fetching the from-location
        fromLocation = getLocation(fromLocationID) if fromLocationID else None

        if fromLocationID and not fromLocation:
            messages.error(request, "From-Location doesn't exist!")
            return HttpResponseRedirect("/product-movements/")

        # Fetching the to-location
        toLocation = getLocation(toLocationID) if toLocationID else None

        if toLocationID and not toLocation:
            messages.error(request, "To-Location doesn't exist!")
            return HttpResponseRedirect("/product-movements/")

        # Fetching the product
        product = getProduct(productID) if productID else None

        if not product:
            messages.error(request, "Product doesn't exist!")
            return HttpResponseRedirect("/products/")

        # Creating a new product movement
        ProductMovement.objects.create(
            from_location = fromLocationID,
            to_location = toLocation,
            product_id = product,
            quantity = quantity
        )
        messages.success(request, "Product Movement added successfully!")
        return HttpResponseRedirect(f"/view-product-movement/{ProductMovement.pk}/")    

    return HttpResponseRedirect("/product-movements/")

def editProductMovement(request):
    """
    A view to edit an existing product movement
    """
    pass

def viewProductMovement(request):
    """
    A view to view an existing product movement
    """
    pass

def report(request):
    """
    A view to report information of products at each location
    """
    locations = Location.objects.all()
    pass

def locationReport(request, locationID):
    """
    A view to report information of products at e specific location
    """
    location = getLocation(locationID)

    if not location:
        messages.error(request, "Location doesn't exist!")
        return HttpResponseRedirect("/locations/")
    pass