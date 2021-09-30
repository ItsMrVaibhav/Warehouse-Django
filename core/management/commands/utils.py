import random
from faker import Faker
from core.models import Location, Product, ProductMovement

fake = Faker(["en_IN"])

def createLocations():
    """
    A function to create random indian locations
    """
    count = 5

    try:
        id = Location.objects.latest("location_id").pk
    except Exception as e:
        print(e)
        id = "-1"

    print(id)
    print("Creating locations")

    for i in range(count):
        id = str(int(id) + 1)
        Location.objects.create(
            location_id = id,
            address = fake.address(),
            pincode = fake.postcode(),
            city = fake.city(),
            state = fake.state(),
            country = fake.country()
        )
        print(f"Status: {((i + 1) / count) * 100}")

    print(f"{count} products created successfully! ")

def createProducts():
    """
    A function to create random products
    """
    count = 5

    try:
        id = Product.objects.latest("product_id").pk
    except:
        id = "-1"

    print("Creating products")
    
    for i in range(count):
        id = str(int(id) + 1)
        Product.objects.create(
            product_id = id,
            name = fake.company(),
            quantity = random.randint(1, 25),
            description = fake.paragraph(nb_sentences = random.randint(5, 15))
        )
        print(f"Status: {((i + 1) / count) * 100}")

    print(f"{count} products created successfully! ")

def getRandomLocation():
    """
    A function to get a combination of two locations to create a product movement
    """
    locations = Location.objects.all()
    toLocation = None if random.randint(0, 1) == 0 else locations.order_by("?").first()

    if toLocation != None:
        locations.exclude(pk = toLocation.pk)
        fromLocation = None if random.randint(0, 1) == 0 else locations.order_by("?").first()
    else:
        fromLocation = locations.order_by("?").first()

    return toLocation, fromLocation

def getRandomProduct():
    """
    A function to get a product with atleast a single product
    """
    products = Product.objects.filter(quantity__gt = 0).order_by("?")
    product = products.first()
    productCount = random.randint(1, product.quantity)
    product.quantity -= productCount
    product.save()
    return product, productCount

def createProductMovements():
    """
    A function to create product movements
    """
    count = 5

    try:
        id = ProductMovement.objects.latest("movement_id").pk
    except:
        id = "-1"

    print("Creating product locations")

    for i in range(count):
        id = str(int(id) + 1)
        toLocation, fromLocation = getRandomLocation()
        product, productCount = getRandomProduct()
        ProductMovement.objects.create(
            movement_id = id,
            from_location = fromLocation,
            to_location = toLocation,
            product_id = product,
            quantity = productCount
        )
        print(f"Status: {((i + 1) / count) * 100}")

    print(f"{count} product locations created successfully! ")