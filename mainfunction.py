import bookclass
import customerclass
from bookstore import Bookstore

bookclass.Book.get_details()
customerclass.Customer.customer_database()
store1 = Bookstore(bookclass.Book.all_books, customerclass.Customer.customer_list)

print("*** WELCOME TO THE PORTAL MAIN PAGE ***")
switch = True
while switch:
    login_option = input("Are you an admin or customer? (Type 'exit' to quit): ").lower()
    if login_option == "admin":
        # (admin menu options)
        print("Choose from the following options:")
        print("1. List all book details")
        print("2. List all customer details")
        print("3. Add a new book to the stock")
        print("4. Restock a book")
        option = int(input("Enter your option: "))
        if option == 1:
            store1.list_books()
        elif option == 2:
            store1.list_customers()
        elif option == 3:
            store1.add_book()
            bookclass.Book.get_details()
        elif option == 4:
            bookclass.Book.get_details()
            book_name = input("Enter the book name to restock: ").lower()
            bookclass.Book.restock(book_name)
        else:
            print("Invalid option. Please try again!")
    elif login_option == "customer":
        print("Choose from the following options:")
        print("1. List all available books")
        print("2. Register as a new customer")
        print("3. Check for a specific book")
        print("4. Purchase books")
        option = int(input("Enter your option: "))
        if option == 1:
            store1.list_books()
        elif option == 2:
            store1.add_customer()
            customerclass.Customer.customer_database()
        elif option == 3:
            book_name = input("Enter the book name: ")
            store1.search_book(book_name)
        elif option == 4:
            registered_customer = input("Are you a registered customer? (yes/no): ").lower()
            if registered_customer == "yes":
                email = input("Enter your registered email: ")
                customer_found = customerclass.Customer.get_customer_by_email(email)
                if customer_found:
                    customer_found.purchase_book()
                else:
                    print("Email not found. Please enter a registered email.")
            elif registered_customer == "no":
                store1.add_customer()
                customerclass.Customer.customer_database()
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            print("Invalid input. Please try again!")
    elif login_option == "exit":
        switch = False
    else:
        print("Invalid option. Please try again!")
