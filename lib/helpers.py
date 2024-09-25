# lib/helpers.py
from models.manufacturer import Manufacturer
from models.product import Product

def list_manufacturer():
    #Retrieve all manufacturers and list them with their index
    manufacturers = Manufacturer.get_all()
    for index, manufacturer in enumerate(manufacturers, start=1):
        print(f"{index}. {manufacturer.name} | Location: {manufacturer.location}")

def add_manufacturer():
    #loop until a valid manufacturer is added or user chooses to go back
    while True:
        name = input("Enter the manufacturer's name (or enter '.' to go back): ").strip()
        if name == '.':
            print("Returning to the previous menu.")
            return
        if not name:
            print("Name cannot be empty. Please enter a valid name.")
            continue    
        if name.isdigit(): #checks if string is all digits
            print("Name cannot be a digit. Please enter a valid name.")
            continue
        if len(name) <= 1 or len(name) >= 15:
            print("Name must be greater than 1 character and less than 15 characters. Please enter a valid name.")
            continue

        #Loop to get a valid location for the manufacturer
        while True:
            location = input("Enter the manufacturer's country location (or enter '.' to go back): ").strip()
            if location == '.':
                print("Returning to the previous menu.")
                return
            if not location:
                print("Location cannot be empty. Please enter a valid location.")
            elif location.isdigit(): # isdigit() checks if string is all digits
                print("Location cannot be all digits. Please enter a valid location.")
            else:
                break

        #Create and save the new manufacturer
        new_manufacturer = Manufacturer.create(name, location)
        new_manufacturer.save()
        print("***********************")
        print(f"Manufacturer '{name}' added.")
        print("***********************")
        break

def delete_manufacturer():
    # List all manufacturers to allow the user to choose one for deletion
    list_manufacturer()
    all_manufacturers = Manufacturer.get_all()
    while True:
        user_input = input("Enter the number of the manufacturer to delete (or '.' to go back): ").strip()
        if user_input == '.':
            print("Returning to the previous menu.")
            return
        try:
            index = int(user_input) - 1
            if 0 <= index < len(all_manufacturers):
                # Remove and delete the selected manufacturer
                deleted_manufacturer = all_manufacturers.pop(index)
                deleted_manufacturer.delete()
                print("***********************")
                print(f"Manufacturer '{deleted_manufacturer.name}' deleted.")
                print("***********************")
                break
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def update_manufacturer():
    # List all manufacturers for the user to update
    list_manufacturer()
    all_manufacturers = Manufacturer.get_all()
    while True:
        user_input = input("Enter the number of the manufacturer to update (or '.' to go back): ").strip()
        if user_input == '.':
            print("Returning to the previous menu.")
            return
        try:
            index = int(user_input) - 1
            if 0 <= index < len(all_manufacturers):
                manufacturer = all_manufacturers[index]

                # Loop to update the manufacturer name
                while True:
                    new_name = input(f"Enter new name for {manufacturer.name} (leave blank to keep current, or '.' to go back): ").strip()
                    if new_name == ".":
                        print("Returning to the previous menu.")
                        return
                    if new_name == "":
                        new_name = manufacturer.name
                        break
                    if new_name.isdigit():
                        print("Name cannot be all digits. Please enter a valid name.")
                        continue
                    if len(new_name) <= 1 or len(new_name) >= 20:
                        print("Name must be greater than 1 character and less than 20 characters.")
                        continue
                    manufacturer.name = new_name
                    break
                
                # Loop to update the manufacturer location
                while True:
                    new_location = input(f"Enter new location for {manufacturer.location} (leave blank to keep current, or '.' to go back): ").strip()
                    if new_location == ".":
                        print("Returning to the previous menu.")
                        return
                    if new_location == "":
                        new_location = manufacturer.location
                        break
                    if new_location.isdigit():
                        print("Location cannot be all digits. Please enter a valid location.")
                        continue
                    manufacturer.location = new_location
                    break

                manufacturer.update() #save the updates

                print("***********************")
                print(f"Manufacturer '{manufacturer.name}' updated.")
                print("***********************")
                break
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def list_product():
    # List all products under each manufacturer
    all_products = Manufacturer.get_all()
    for manufacturer in all_products:
        print("---------------------------------------------------------------------")
        print(f"{manufacturer.name} (Location: {manufacturer.location})")
        manufacturer_products = manufacturer.product()
        for index, product in enumerate(manufacturer_products):
            print(f"  {index + 1}. Category: {product.category} | Model: {product.model} | Quantity: {product.quantity}")
        print("---------------------------------------------------------------------")

def add_product():
    # Loop to add a new product for a selected manufacturer
    while True:
        all_manufacturers = Manufacturer.get_all()
        list_manufacturer()

        user_input = input("Enter the number of the manufacturer to add a product for (or '.' to go back): ").strip()
        
        if user_input == ".":
            print("Returning to the previous menu.")
            return

        try:
            index = int(user_input) - 1 # Convert input to an index
            if 0 <= index < len(all_manufacturers):
                manufacturer = all_manufacturers[index]
                # Loop to  get a valid product category
                while True:
                    category = input("Enter the category (or '.' to go back): ").strip()
                    if category == ".":
                        print("Returning to the previous menu.")
                        return
                    if len(category) < 2 or len(category) > 25:
                        print("category must be at least 2 characters and less than 25 characters long.")
                    elif category.isdigit():
                        print("category cannot be all digits. Please enter a valid category.")
                    else:
                        break
                #Loop for a valid product model
                while True:
                    model = input("Enter the model (or '.' to go back): ").strip()
                    if model == ".":
                        print("Returning to the previous menu.")
                        return
                    if len(model) < 2 or len(model) > 25:
                        print("Model must be at least 2 characters and less than 25 characters long.")
                    elif model.isdigit():
                        print("Model cannot be all digits. Please enter a valid model.")
                    else:
                        break
                #loop to get a valid product quantity
                while True:
                    quantity = input("Enter the quantity (an integer, or '.' to go back): ").strip()

                    if quantity == ".":
                        print("Returning to the previous menu.")
                        return

                    if quantity.isdigit() and 0 <= int(quantity) <= 99999:
                        quantity = int(quantity)  # Convert the valid string to an integer
                        break
                    else:
                        print("Invalid quantity. Please enter an integer between 0 and 99999.")

                # Create and save the new product
                product = Product(category=category, model=model, quantity=quantity, manufacturer_id=manufacturer.id)
                product.save()
                print("***********************")
                print(f"Product '{model}' added for {manufacturer.name}.")
                break
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input: Please enter a valid number.")

def delete_product():
    # Allow the user to delete a product for a selected manufacturer
    while True:
        all_manufacturers = Manufacturer.get_all()
        list_manufacturer()
        
        user_input = input("Enter the number of the manufacturer to delete a product for (or '.' to go back): ").strip()
        if user_input == ".":
            print("Returning to the previous menu.")
            return
        try:
            manufacturer_index = int(user_input) - 1
            if 0 <= manufacturer_index < len(all_manufacturers):
                manufacturer = all_manufacturers[manufacturer_index]
                manufacturer_products = manufacturer.product()
                
                # Loop to select a product to delete
                while True:
                    for index, product in enumerate(manufacturer_products):
                        print(f"  {index + 1}. Category: {product.category} | Model: {product.model} | Quantity: {product.quantity}")
                    
                    user_input = input("Enter the number of the product to delete (or '.' to go back): ").strip()
                    if user_input == ".":
                        print("Returning to the previous menu.")
                        break
                    try:
                        product_index = int(user_input) - 1
                        if 0 <= product_index < len(manufacturer_products):
                            deleted_product = manufacturer_products[product_index]
                            deleted_product.delete()
                            print("***********************")
                            print(f"product '{deleted_product.model}' deleted from {manufacturer.name}.")
                            print("***********************")
                            break
                        else:
                            print("Invalid selection. Please enter a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                break
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def update_product():
    # Allow the user to update a product for a selected manufacturer
    while True:
        all_manufacturers = Manufacturer.get_all()
        list_manufacturer()
        
        manufacturer_input = input("Enter the number of the manufacturer to update a product for (or '.' to go back): ").strip()
        if manufacturer_input == ".":
            return 
        try:
            manufacturer_index = int(manufacturer_input) - 1
            if 0 <= manufacturer_index < len(all_manufacturers):
                manufacturer = all_manufacturers[manufacturer_index]
                manufacturer_products = manufacturer.product()
                
                # Loop to select a product to update
                while True:
                    for index, product in enumerate(manufacturer_products):
                        print(f"  {index + 1}. Category: {product.category} | Model: {product.model} | Quantity: {product.quantity}")
                    
                    product_input = input("Enter the number of the product to update (or '.' to go back): ").strip()
                    if product_input == ".":
                        print("Returning to the previous menu.")
                        break
                    try:
                        product_index = int(product_input) - 1
                        if 0 <= product_index < len(manufacturer_products):
                            product = manufacturer_products[product_index]

                            new_category = input(f"Enter new category name for '{product.category}' (leave blank to keep current, or '.' to go back): ").strip()
                            if new_category == ".":
                                return
                            if new_category:
                                product.category = new_category

                            new_model = input(f"Enter new model for '{product.model}' (leave blank to keep current, or '.' to go back): ").strip()
                            if new_model == ".":
                                return
                            if new_model:
                                product.model = new_model

                            new_quantity = input(f"Enter new quantity for '{product.quantity}' (leave blank to keep current, or '.' to go back): ").strip()
                            if new_quantity == ".":
                                return
                            if new_quantity.isdigit():
                                product.quantity = int(new_quantity)

                            product.update()
                            print("***********************")
                            print(f"Product '{product.model}' updated.")
                            print("***********************")
                            break
                        else:
                            print("Invalid selection. Please enter a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                return
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        
def exit_program():
    # Exit the program 
    print("Goodbye!")
    exit()
