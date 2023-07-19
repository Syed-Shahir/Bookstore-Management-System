import bookclass

from bookclass import Book

import csv

class Customer:
    customer_list = []

    def __init__(self, name: str, email: str, acc_bal: float):
        """Initialize a customer object with its details."""
        self.name = name
        self.email = email
        self.acc_bal = acc_bal
        Customer.customer_list.append(self)

    @classmethod
    def customer_database(cls):
        """Read customer details from the CSV file and populate the customer_list."""
        Customer.customer_list.clear()
        path = "project1custom.csv"
        with open(path, "r") as file:
            data = csv.DictReader(file)
            for row in data:
                name = row.get('name')
                email = row.get('email')
                balance = float(row.get('balance'))
                Customer(name, email, balance)

    @classmethod
    def get_customer_by_email(cls, email: str):
        """Find and return a customer object by email."""
        for customer_obj in cls.customer_list:
            if customer_obj.email.lower() == email.lower():
                return customer_obj
        return None

    def purchase_book(self):
        """Process a book purchase for the customer."""
        book_list = bookclass.Book.all_books
        print("****************MENU************************")
        print(f"Title       |  Author    |  Price|  ISBN      | Quantity")
        for value in book_list:
            print(f"{value.title:10}  | {value.author:10}  | {value.price:5}  | {value.isbn:10}  | {value.quantity:2}")

        total_bill = 0.0
        while True:
            book_title = input("Enter the title of the book to purchase (or 'exit' to stop): ").lower()
            if book_title == "exit":
                break

            found_book = None
            for book_obj in book_list:
                if book_obj.title.lower() == book_title:
                    found_book = book_obj
                    break

            if found_book is None:
                print("Book not found. Please enter a valid book title.")
                continue

            quantity_to_buy = int(input("Enter the quantity to buy: "))
            if quantity_to_buy <= 0:
                print("Invalid quantity. Please enter a positive number.")
                continue
            elif quantity_to_buy > found_book.quantity:
                print("Insufficient quantity in stock. Please enter a lower quantity.")
                continue

            total_price = found_book.price * quantity_to_buy
            total_bill += total_price
            found_book.sell_book(quantity_to_buy)

        print(f"Your total bill is: {total_bill:.2f}")
        print(f"Your account balance is: {self.acc_bal:.2f}")
        if total_bill > self.acc_bal:
            print("You have insufficient balance.")
        else:
            self.acc_bal -= total_bill
            self.update_balance_in_csv()
            print("Purchase successful.")

    def update_balance_in_csv(self):
        """Update the CSV file with the new customer balance."""
        path = "project1custom.csv"
        with open(path, "r", newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        # Find the row with the matching customer email and update the balance
        for row in rows:
            if row["email"].lower() == self.email.lower():
                row["balance"] = str(self.acc_bal)

        # Write the updated data back to the CSV file
        with open(path, "w", newline='') as file:
            fieldnames = ["name", "email", "balance"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
