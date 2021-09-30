from django.core.management.base import BaseCommand
from .utils import createLocations, createProducts, createProductMovements

class Command(BaseCommand):
    help = "Generate dummy data"

    def handle(self, *args, **kwargs):
        createLocations()
        createProducts()
        createProductMovements()