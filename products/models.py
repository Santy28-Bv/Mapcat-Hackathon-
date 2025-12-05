 
# Modelo para productos

# app/models/product.py

class Product:
    def __init__(self, id, name,category, price, url_image, sku, stock, subcategory, supplier,
                 rental_enabled=False, rental_monthly_price=0,
                 rental_min_months=0, rental_status="available",
                 rented_to=None, rental_end_date=None):
        
        self.id = id
        self.name = name
        self.price = price
        self.sku = sku
        self.stock = stock
        self.url_image = url_image
        self.subcategory = subcategory
        self.supplier = supplier
        self.rental_enabled = rental_enabled
        self.rental_monthly_price = rental_monthly_price
        self.rental_min_months = rental_min_months
        self.rental_status = rental_status
        self.rented_to = rented_to
        self.rental_end_date = rental_end_date
        self.category = category

    def to_dict(self):
        return self.__dict__

class Category:
    def __init__(self, id, name,description):
        self.id = id
        self.name = name 
        self.description = description

        def to_dict(self):
            return self.__dict__

class SubCategory:
    def __init__(self, id, name, description, from_category):
        self.id = id
        self.name = name 
        self.description = description
        self.from_category = from_category
        def to_dict(self):
            return self.__dict__