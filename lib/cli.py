from seed import seed
from helpers import (
    list_manufacturer,
    add_manufacturer,
    delete_manufacturer,
    update_manufacturer,
    list_product,
    add_product,
    delete_product,
    update_product,
    find_manufacturer_by_name,
    find_product_by_category,
    exit_program,
)

# This function displays the main menu options to the user.
def main_page():
    print("*********************************************************************")
    print("*                          INVENTORY MANAGER                        *")
    print("*********************************************************************")
    print("*                     Welcome to Inventory Manager!                 *")
    print("*********************************************************************")
    print("*                      Please choose from the following:            *")
    print("*********************************************************************")
    print("*                 Press V to View All Manufacturers                 *")
    print("*                 Press M to Manage and View Products               *")
    print("*                 Press E to Exit App                               *")
    print("---------------------------------------------------------------------")

# This function handles viewing and managing manufacturers.
def view_manufacturers():
    while True:
        list_manufacturer()
        print("*********************************************************************")
        print("*                         MANAGE Manufacturers                      *")
        print("*********************************************************************")
        print("*                Please choose from the following:                  *")
        print("*********************************************************************")
        print("*                  Press 1.  Add New Manufacutrer                   *")
        print("*                  Press 2.  Delete a Manufacutrer                  *")
        print("*                  Press 3.  Update a Manufacutrer                  *")
        print("*                  Press 4.  Find a Manufacutrer by Name            *")
        print("*                  Press 5.  Manage Products                        *")
        print("*                  Press 6.  Back to Main Menu                      *")
        print("---------------------------------------------------------------------")

        # Captures the user's choice and calls the corresponding function
        choice = input("Enter your choice: ")
        if choice == '1':
            add_manufacturer()
        elif choice == '2':
            delete_manufacturer()
        elif choice == '3':
            update_manufacturer()
        elif choice == '4':
            find_manufacturer_by_name()
        elif choice == '5':
            manage_product()  
        elif choice == '6':
            main()
        else:
            print("Invalid choice, please try again.")

# This function handles viewing and managing products.
def manage_product():
    while True:
        print("******************************************************************")
        print("*                          MANAGE Products                       *")
        print("******************************************************************")
        print("*                Please choose from the following:               *")
        print("******************************************************************")
        print("*                  Press 1.  View All Product                    *")
        print("*                  Press 2.  Add New Product                     *")
        print("*                  Press 3.  Delete a Product                    *")
        print("*                  Press 4.  Update a Product                    *")
        print("*                  Press 5.  Find a Product by Category          *")
        print("*                  Press 6.  View manufacturers                  *")
        print("*                  Press 7.  Back to Main Menu                   *")
        print("------------------------------------------------------------------")

        # Captures the user's choice and calls the corresponding function
        choice = input("Enter your choice: ")
        if choice == '1':
            list_product()
        elif choice == '2':
            add_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            update_product()
        elif choice == '5':
            find_product_by_category()
        elif choice == '6':
            view_manufacturers() 
        elif choice == '7':
            main()
        else:
            print("Invalid choice, please try again.")

# Main function that runs the application and provides access to the main menu.
def main():
    while True:
        main_page()
        choice = input("> ").lower()
        if choice == 'v':
            view_manufacturers()
        elif choice == 'm':
            manage_product()
        elif choice == 'e':
            exit_program()
        else:
            print("Invalid choice, please try again.")

# Entry point for the script. This ensures that the program runs when the script is executed directly.
if __name__ == "__main__":
    main()