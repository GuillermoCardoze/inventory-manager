# lib/models/manufacturer.py
from models.__init__ import CONN, CURSOR
from models.product import Product 

class Manufacturer:

    # Constructor initializes the Manufacturer instance with a name, location, and optional id.
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name  # Uses the name setter method for validation
        self.location = location  # Uses the location setter method for validation

    # Getter for the 'name' attribute.
    @property
    def name(self):
        return self._name

    # Setter for 'name' with validation: the name must be a string between 2 and 15 characters.
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 < len(name) < 15:
            self._name = name
        else:
            raise ValueError("Name must be greater than 1 character and less than 15 characters. Please enter a valid name.")
    
    # Getter for the 'location' attribute.
    @property
    def location(self):
        return self._location

    # Setter for 'location' with validation: the location must be a non-empty string.
    @location.setter
    def location(self, location):
        if isinstance(location, str) and location.strip():
            self._location = location
        else:
            raise ValueError("Location must be a country. Please enter a valid location.")

    # Class method to create the 'manufacturer' table in the database if it doesn't already exist.
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

    # Class method to drop the 'manufacturer' table if it exists.
    @classmethod 
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS manufacturer"
        CURSOR.execute(sql)  
        CONN.commit() 

    # Saves the Manufacturer instance to the database. If it has an 'id', it updates the existing record; otherwise, it inserts a new record.
    def save(self): 
        if self.id:
            self.update()
        else:
            sql = "INSERT INTO manufacturer (name, location) VALUES (?, ?)"
            CURSOR.execute(sql, (self.name, self.location))  # Inserts a new record into the manufacturer table
            CONN.commit()
            self.id = CURSOR.lastrowid 

    # Class method to create and save a new Manufacturer instance in the database.
    @classmethod 
    def create(cls, name, location=None):
        manufacturer = cls(name, location) 
        manufacturer.save()  
        return manufacturer
    
    # Updates the existing Manufacturer record in the database with new name and location.
    def update(self): 
        sql = "UPDATE manufacturer SET name = ?, location = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.location, self.id)) 
        CONN.commit()  

    # Deletes the Manufacturer instance from the database.
    def delete(self): 
        sql = "DELETE FROM manufacturer WHERE id = ?"
        CURSOR.execute(sql, (self.id,)) 
        CONN.commit()  
        self.id = None  # Sets the 'id' to None after deletion

    # Class method to instantiate a Manufacturer object from a database row.
    @classmethod 
    def instance_from_db(cls, row):
        manufacturer = cls(row[1], row[2], row[0])  # Creates a Manufacturer instance using data from the row
        return manufacturer  
    
    # Class method to retrieve all Manufacturer records from the database.
    @classmethod 
    def get_all(cls):
        sql = "SELECT * FROM manufacturer"
        rows = CURSOR.execute(sql).fetchall() 
        return [cls.instance_from_db(row) for row in rows]  # Returns a list of Manufacturer instances
    
    # Class method to find a Manufacturer by name (case-insensitive).
    # @classmethod
    # def find_by_name(cls, name):
    #     name = name.lower()  
    #     sql = "SELECT * FROM manufacturer WHERE LOWER(name) = ?"
    #     row = CURSOR.execute(sql, (name,)).fetchone()  
    #     return cls.instance_from_db(row) if row else None  # Returns the Manufacturer instance if found
    
    # # Class method to find a Manufacturer by its 'id'.
    # @classmethod
    # def find_by_id(cls, id):
    #     sql = "SELECT * FROM manufacturer WHERE id = ?"
    #     row = CURSOR.execute(sql, (id,)).fetchone() 
    #     return cls.instance_from_db(row) if row else None  # Returns the Manufacturer instance if found
    
    # Retrieves all Products associated with this Manufacturer using the 'manufacturer_id' foreign key.
    def product(self):
       from models.product import Product  # Importing Product class to avoid circular imports at the top
       sql = "SELECT * FROM product WHERE manufacturer_id = ?"  # Fetches products where the manufacturer_id matches this Manufacturer's id
       CURSOR.execute(sql, (self.id,))
       rows = CURSOR.fetchall()  
       return [Product.instance_from_db(row) for row in rows]  # Returns a list of Product instances associated with this Manufacturer
