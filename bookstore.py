import csv
from bookclass import Book
from customerclass import Customer

class Bookstore:
    def __init__(self, list1: list, list2: list):
        """Initialize the bookstore with book and customer data."""
        self.books_list = list1
        self.customer_data = list2

    def list_customers(self):
        """List all customers' details."""
        Customer.customer_database()
        print(f"Customer              | Email          | Balance")
        for value in Customer.customer_list:
            print(f"{value.name:20}  | {value.email:30}  | {value.acc_bal}")

    def list_books(self):
        """List all available book details."""
        Book.get_details()
        print("****************MENU************************")
        print(f"Title       |  Author    |  Price|  ISBN      | Quantity")
        for value in Book.all_books:
            print(f"{value.title:10}  | {value.author:10}  | {value.price:5}  | {value.isbn:10}  | {value.quantity:2}")

    def search_book(self, book_name: str):
        """Search for a book by its name and display its details."""
        found_book = None
        for book_obj in Book.all_books:
            if book_obj.title.lower() == book_name.lower():
                found_book = book_obj
                break

        if found_book is not None:
            print(f"This {book_name} is available with the following details:")
            print(f"Title       |  Author    |  Price|  ISBN      | Quantity")
            print(f"{found_book.title:10}  | {found_book.author:10}  | {found_book.price:5}  | {found_book.isbn:10}  | {found_book.quantity:2}")
        else:
            print("Book is not available.")

    @classmethod
    def add_book(cls):
        """Add a new book to the stock and update the CSV file."""
        path = "project1oop.csv"
        with open(path, "a", newline='') as file:
            writer = csv.writer(file)

            # Get book details from the user
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            price = float(input("Enter the price: "))
            isbn = input("Enter the ISBN: ")
            quantity = int(input("Enter the quantity: "))

            # Write the book details as a new row in the CSV file
            writer.writerow([title, author, price, isbn, quantity])

    @classmethod
    def add_customer(cls):
        """Add a new customer to the system and update the CSV file."""
        path = "project1custom.csv"
        with open(path, "a", newline="") as file:
            writer = csv.writer(file)
            print("Enter new account details:")
            name = input("Enter your name: ")
            email = input("Enter your email address: ")
            balance = float(input("Enter your account balance: "))

            writer.writerow([name, email, balance])
