from models.manufacturer import Manufacturer
from models.product import Product

def seed():
    # Initialize database tables
    Manufacturer.drop_table()
    Product.drop_table()
    Manufacturer.create_table()
    Product.create_table()

    ford = Manufacturer.create(name="Ford", location="USA")    
    chevrolete = Manufacturer.create(name="Chevrolete", location="USA")    
    farrari = Manufacturer.create(name="Farrari", location="Italy")
    bmw = Manufacturer.create(name="BMW", location="Germany")

    Product.create(category="SUV", model="Expedition", quantity=3, manufacturer_id=ford.id)
    Product.create(category="Car", model="Mustang", quantity=2, manufacturer_id=ford.id)
    Product.create(category="SUV", model="Suburban", quantity=4, manufacturer_id=chevrolete.id)
    Product.create(category="Car", model="Camaro", quantity=5, manufacturer_id=chevrolete.id)
    Product.create(category="SUV", model="Purosangue", quantity=1, manufacturer_id=farrari.id)
    Product.create(category="Car", model="SF90", quantity=7, manufacturer_id=farrari.id)
    Product.create(category="SUV", model="X6", quantity=9, manufacturer_id=bmw.id)
    Product.create(category="Car", model="M3", quantity=4, manufacturer_id=bmw.id)

    print("Seeding Successful!")

seed()