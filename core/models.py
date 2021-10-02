from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length = 100, primary_key = True)
    name = models.CharField(max_length = 200)
    description = models.TextField(max_length = 2500)
    dateCreated = models.DateTimeField(auto_now_add = True, verbose_name = "Created")
    dateModified = models.DateTimeField(auto_now = True, verbose_name = "Modified")

    def __str__(self):
        return f"{self.product_id} |{self.name}"

    class Meta:
        ordering = ["-dateCreated"]

class Location(models.Model):
    location_id = models.CharField(max_length = 100, primary_key = True, verbose_name = "Location ID")
    name = models.CharField(max_length = 250)
    address = models.CharField(max_length = 250)
    pincode = models.CharField(max_length = 6)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    dateCreated = models.DateTimeField(auto_now_add = True, verbose_name = "Created")
    dateModified = models.DateTimeField(auto_now = True, verbose_name = "Modified")

    def getFullAddress(self):
        return f"{self.address} {self.pincode}, {self.city}, {self.state}, {self.country}"

    def __str__(self):
        return f"{self.location_id} |{self.getFullAddress()}"

    class Meta:
        ordering = ["-dateCreated"]

class ProductMovement(models.Model):
    typeChoices = (
        ("MI", "Moved In"),
        ("MO", "Moved Out"),
        ("TR", "Transfer")
    )
    movement_id = models.CharField(max_length = 100, primary_key = True, verbose_name = "Movement ID")
    from_location = models.ForeignKey(Location, on_delete = models.CASCADE, null = True, related_name = "sources")
    to_location = models.ForeignKey(Location, on_delete = models.CASCADE, null = True, related_name = "destinations")
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "movements")
    quantity = models.IntegerField()
    dateCreated = models.DateTimeField(auto_now_add = True, verbose_name = "Created")
    dateModified = models.DateTimeField(auto_now = True, verbose_name = "Modified")
    type = models.CharField(max_length = 5, choices = typeChoices, default = "TR")

    def __str__(self):
        return f"{self.from_location.pk if self.from_location else 'X'} --> {self.to_location.pk if self.to_location else 'X'} | {self.product_id.name} ({self.product_id.pk}) | {self.quantity}"

    class Meta:
        ordering = ["-dateCreated"]
        verbose_name = "ProductMovement"
        verbose_name_plural = "ProductMovements"