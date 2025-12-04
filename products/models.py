 
# Modelo para productos

# app/models/product.py

class Product:
    def __init__(self, id, name, price, stock, category, supplier,
                 rental_enabled=False, rental_monthly_price=0,
                 rental_min_months=0, rental_status="available",
                 rented_to=None, rental_end_date=None):
        
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.supplier = supplier
        self.rental_enabled = rental_enabled
        self.rental_monthly_price = rental_monthly_price
        self.rental_min_months = rental_min_months
        self.rental_status = rental_status
        self.rented_to = rented_to
        self.rental_end_date = rental_end_date

    def to_dict(self):
        return self.__dict__

class Category:
    def __init__(self, id, name,description):
        self.id = id
        self.name = name 
        self.description = description

        def to_dict(self):
            return self.__dict__