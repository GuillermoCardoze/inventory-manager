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
    exit_program,
)

# This function displays the main menu options to the user.
def main_page():
    stars()
    print("   Welcome to Inventory Manager!   ")
    stars()
    print("   Choose from the following:   ")
    stars()
    print("   Press V to View All Manufacturers   ")
    print("   Press M to Manage and View Products   ")
    print("   Press E to Exit App   ")
    dashes()

# This function handles viewing and managing manufacturers.
def view_manufacturers():
    while True:
        list_manufacturer()
        stars()
        print("   MANAGE Manufacturers   ")
        stars()
        print("   Choose from the following:   ")
        stars()
        print("   Press 1.  Add New Manufacutrer   ")
        print("   Press 2.  Delete a Manufacutrer   ")
        print("   Press 3.  Update a Manufacutrer   ")
        print("   Press 4.  Manage Products   ")
        print("   Press 5.  Back to Main Menu   ")
        dashes()

        # Captures the user's choice and calls the corresponding function
        choice = input("Enter your choice: ")
        if choice == '1':
            add_manufacturer()
        elif choice == '2':
            delete_manufacturer()
        elif choice == '3':
            update_manufacturer()
        elif choice == '4':
            manage_product()  
        elif choice == '5':
            main()
        else:
            print("Invalid choice, please try again.")

# This function handles viewing and managing products.
def manage_product():
    while True:
        stars()
        print("   MANAGE Products   ")
        stars()         
        print("   Choose from the following:   ")
        stars()
        print("   Press 1.  View All Product   ")
        print("   Press 2.  Add New Product   ")
        print("   Press 3.  Delete a Product   ")
        print("   Press 4.  Update a Product   ")
        print("   Press 5.  View manufacturers   ")
        print("   Press 6.  Back to Main Menu   ")
        dashes()

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
            view_manufacturers() 
        elif choice == '6':
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

def dashes():
    print("------------------------------")   

def stars():
    print("******************************")

# Entry point for the script. This ensures that the program runs when the script is executed directly.
if __name__ == "__main__":
    main()