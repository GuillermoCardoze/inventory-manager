# lib/models/product.py
from models.__init__ import CONN, CURSOR


class Product:
    
    def __init__(self, category, model, quantity, manufacturer_id=0, id=None):
        self.id = id
        self.category = category
        self.model = model
        self.quantity = quantity
        self.manufacturer_id = manufacturer_id
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and 2 <= len(category) <= 25:
            self._category = category
        else:
            raise ValueError("Task must be at least 2 characters and less than 25 characters long.") 
        
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if isinstance(model, str) and model.strip():
            self._model = model
        else:
            raise ValueError("model cannot be empty. Please enter a valid model.")


    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            self._quantity = quantity
        else:
            raise ValueError("Quantity must be a non-negative integer.")
        
    @property
    def manufacturer_id(self):
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, manufacturer_id):
        if isinstance(manufacturer_id, int) and manufacturer_id > 0:
            self._manufacturer_id = manufacturer_id
        else:
            raise ValueError("Manufacturer ID must be a positive integer.")

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

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS product"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id:
            self.update()
        else:
            sql = """
                INSERT INTO product (category, model, quantity, manufacturer_id)
                VALUES (?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.category, self.model, self.quantity, self.manufacturer_id))
            CONN.commit()
            self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, category, model, quantity, manufacturer_id):
        product = cls(category, model, quantity, manufacturer_id)
        product.save()
        return product
    
    def update(self):
        sql = """
            UPDATE product
            SET category = ?, model = ?, quantity = ?, manufacturer_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.category, self.model, self.quantity, self.manufacturer_id, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM product WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        product = cls(row[1], row[2], row[3], row[4], row[0])
        return product
    
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM product"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    
    @classmethod
    def find_by_category(cls, category):
        category = category.lower()
        sql = "SELECT * FROM product WHERE LOWER(category) = ?"
        rows = CURSOR.execute(sql, (category,)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else []

    @classmethod
    def get_all_categories(cls):
        sql = "SELECT DISTINCT category FROM product"
        rows = CURSOR.execute(sql).fetchall()
        return [row[0] for row in rows] if rows else []
