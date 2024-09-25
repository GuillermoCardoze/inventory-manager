# lib/models/product.py
from models.__init__ import CONN, CURSOR


class Product:

    # The constructor initializes the product attributes. If `id` is not provided, it is set to None.
    # `manufacturer_id` is optional and defaults to 0.
    def __init__(self, category, model, quantity, manufacturer_id=0, id=None):
        self.id = id
        self.category = category
        self.model = model
        self.quantity = quantity
        self.manufacturer_id = manufacturer_id
    
    # Getter for 'category' attribute
    @property
    def category(self):
        return self._category
    
    # Setter for 'category' with validation: must be a string and have a length between 2 and 25 characters.
    @category.setter
    def category(self, category):
        if isinstance(category, str) and 2 <= len(category) <= 25:
            self._category = category
        else:
            raise ValueError("Task must be at least 2 characters and less than 25 characters long.") 

    # Getter for 'model' attribute   
    @property
    def model(self):
        return self._model
    
    # Setter for 'model' with validation: must be a non-empty string.
    @model.setter
    def model(self, model):
        if isinstance(model, str) and model.strip():
            self._model = model
        else:
            raise ValueError("model cannot be empty. Please enter a valid model.")

    # Getter for 'quantity' attribute
    @property
    def quantity(self):
        return self._quantity

    # Setter for 'quantity' with validation: must be a non-negative integer.
    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            self._quantity = quantity
        else:
            raise ValueError("Quantity must be a non-negative integer.")

    # ONE SOURCE OF TRUTH: Product (many) references Manufacturer (one) by manufacturer_id.
    # This ensures that each product refers to the manufacturer without duplicating data.
    @property
    def manufacturer_id(self):
        return self._manufacturer_id

    # Setter for 'manufacturer_id' with validation: must be a positive integer.
    @manufacturer_id.setter
    def manufacturer_id(self, manufacturer_id):
        if isinstance(manufacturer_id, int) and manufacturer_id > 0:
            self._manufacturer_id = manufacturer_id
        else:
            raise ValueError("Manufacturer ID must be a positive integer.")

    # Class method to create the 'product' table in the database if it doesn't exist.
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY,
                category TEXT,
                model TEXT,
                quantity INTEGER,
                manufacturer_id INTEGER,
                FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    # Class method to drop the 'product' table if it exists. This is used for cleanup.
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS product"
        CURSOR.execute(sql)
        CONN.commit()

    #ORM LIKE METHODS SAVE, CREATE, UPDATE, DELETE
    # Saves the product to the database. If the product has an 'id', it updates the record; otherwise, it inserts a new record.
    def save(self):
        if self.id:
            self.update() # If the product already has an 'id', update the existing record
        else:
            sql = """
                INSERT INTO product (category, model, quantity, manufacturer_id)
                VALUES (?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.category, self.model, self.quantity, self.manufacturer_id))
            CONN.commit()
            self.id = CURSOR.lastrowid # Set the product's 'id' to the last inserted row's id

    # Class method to create a new product instance and save it to the database.
    @classmethod
    def create(cls, category, model, quantity, manufacturer_id):
        product = cls(category, model, quantity, manufacturer_id)
        product.save()
        return product
    
    # Updates an existing product record in the database based on its 'id'.
    def update(self):
        sql = """
            UPDATE product
            SET category = ?, model = ?, quantity = ?, manufacturer_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.category, self.model, self.quantity, self.manufacturer_id, self.id))
        CONN.commit()

    # Deletes the product from the database and resets the 'id' to None.
    def delete(self):
        sql = "DELETE FROM product WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None

    # Class method to instantiate a Product object from a database row.
    @classmethod
    def instance_from_db(cls, row):
        product = cls(row[1], row[2], row[3], row[4], row[0])
        return product
    
    # Class method to retrieve all products from the database.
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM product"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    # Class method to find all products with a specific category.
    # @classmethod
    # def find_by_category(cls, category):
    #     category = category.lower()
    #     sql = "SELECT * FROM product WHERE LOWER(category) = ?"
    #     rows = CURSOR.execute(sql, (category,)).fetchall()
    #     return [cls.instance_from_db(row) for row in rows] if rows else []

    # # Class method to retrieve all distinct categories from the database.
    # @classmethod
    # def get_all_categories(cls):
    #     sql = "SELECT DISTINCT category FROM product"
    #     rows = CURSOR.execute(sql).fetchall()
    #     return [row[0] for row in rows] if rows else []
