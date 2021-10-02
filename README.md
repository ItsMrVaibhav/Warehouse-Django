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
1. First, create some database migrations using `python manage.py makemigrations` and then migrate them using `python manage.py migrate`
2. Create a superuser using the following `python manage.py createsuperuser` and fill the required details.
3. Admin panel can be accessed at this URL - `http://127.0.0.1:8000/admin/`
4. Run the server using `python manage.py runserver`