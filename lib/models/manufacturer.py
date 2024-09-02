from models.__init__ import CONN, CURSOR

class Manufacturer:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self. location = location

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 < len(name) < 15:
            self._name = name
        else:
            raise ValueError("Name must be greater than 1 character and less than 15 characters. Please enter a valid name.")
    
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, location):
        if isinstance(location, str) and location.strip():
            self._location = location
        else:
            raise ValueError("Location must be a city and state. Please enter Valid location. ")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS manufacturer (
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS manufacturer"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id:
            self.update()
        else:
            sql = "INSERT INTO manufacturer (name, location) VALUES (?, ?)"
            CURSOR.execute(sql, (self.name, self.location))
            CONN.commit()
            self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, location=None):
        manufacturer = cls(name, location)
        manufacturer.save()
        return manufacturer
    
    def update(self):
        sql = "UPDATE manufacture SET name = ?, location = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM manufacturer WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        manufacturer = cls(row[1], row[2], row[0])
        return manufacturer
    
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM manufacturer"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        name = name.lower()
        sql = "SELECT * FROM manufacturer WHERE LOWER(name) = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM manufacturer WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def product(self):
       from models.product import Product
       sql = "SELECT * FROM product WHERE manufacturer_id = ?"
       CURSOR.execute(sql, (self.id,))
       rows = CURSOR.fetchall()
       return [Product.instance_from_db(row) for row in rows]