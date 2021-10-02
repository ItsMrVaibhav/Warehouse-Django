# Warehouse - Django
A products/inventory management system. The application supports adding products, locations, and product movements. A user can perform CRUD operations over products, locations, and product movements.

For testing purposes, sample data can be created using the command `python manage.py generatedata` .Apart from that, one can use either the web application or the admin panel.

## How to setup?
1. Install `Python 3.8.9`
2. Run `pip install virtualenv`
3. Create a virtual environment using `virtualenv environment`
4. Activate the virtual environment using `environment\Scripts\activate`. This will only work for Windows.
5. Install the dependencies using `pip install -r requirements.txt`

## How to run the project?
1. First, create some database migrations using `python manage.py makemigrations core` and then migrate them using `python manage.py migrate`
2. Create a superuser using the following `python manage.py createsuperuser` and fill the required details.
3. Admin panel can be accessed at this URL - `http://127.0.0.1:8000/admin/`
4. Run the server using `python manage.py runserver`

## Sample Video
Link to the video - https://youtu.be/JzWdKGz9rJg

## Screenshots
### Add Product
![Add Product](/README/add-product.png "Add Product")

### View Product
![View Product](/README/view-product.png "View Product")

### Edit Product
![Edit Product](/README/edit-product.png "Edit Product")

### Add Location
![Add Location](/README/add-location.png "Add Location")

### View Location
![View Location](/README/view-location.png "View Location")

### Edit Location
![Edit Location](/README/edit-location.png "Edit Location")

### Product Movements Grid/Report/Overview
![Product Movements Grid/Report/Overview](/README/movements-grid.png "Product Movements Grid/Report/Overview")

### Add Product Movement (Move In)
![Add Product Movement (Move In)](/README/movement-1.1.png "Add Product Movement (Move In)")

### Add Product Movement (Move Out)
![Add Product Movement (Move Out)](/README/movement-2.1.png "Add Product Movement (Move Out)")

### Add Product Movement (Transfer)
![Add Product Movement (Transfer)](/README/movement-3.1.png "Add Product Movement (Transfer)")

### View Product Movement (Move In)
![View Product Movement (Move In)](/README/movement-1.2.png "View Product Movement (Move In)")

### View Product Movement (Move Out)
![View Product Movement (Move Out)](/README/movement-2.2.png "View Product Movement (Move Out)")

### View Product Movement (Transfer)
![View Product Movement (Transfer)](/README/movement-3.2.png "View Product Movement (Transfer)")

### Edit Product Movement (Move In)
![Edit Product Movement ](/README/movement-1.3.png "Edit Product Movement (Move In)")

### Edit Product Movement (Move Out)
![Edit Product Movement (Move Out)](/README/movement-2.3.png "Edit Product Movement (Move Out)")

### Edit Product Movement (Transfer)
![Edit Product Movement (Transfer)](/README/movement-3.3.png "Edit Product Movement (Transfer)")
