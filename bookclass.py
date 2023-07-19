import csv

class Book:
    all_books = []

    def __init__(self, title: str, author: str, price: float, isbn: str, quantity: int):
        """Initialize a book object with its details."""
        self.title = title
        self.author = author
        self.price = price
        self.isbn = isbn
        self.quantity = quantity
        Book.all_books.append(self)

    @classmethod
    def get_details(cls):
        """Read book details from the CSV file and populate the all_books list."""
        Book.all_books.clear()
        path = "project1oop.csv"
        with open(path, "r") as file:
            data = csv.DictReader(file)
            for row in data:
                title = row.get('title')
                author = row.get('author')
                price = float(row.get('price'))
                isbn = row.get('isbn')
                quantity = int(row.get('quantity'))
                Book(title, author, price, isbn, quantity)

    def sell_book(self, quantity_to_sell: int) -> float:
        """Sell a certain quantity of the book and update the quantity in the CSV file.

        Args:
            quantity_to_sell (int): The quantity of the book to be sold.

        Returns:
            float: Total price for the sold quantity.
        """
        if quantity_to_sell <= self.quantity:
            self.quantity -= quantity_to_sell
            self.update_quantity_in_csv()
            return quantity_to_sell * self.price
        else:
            print("Insufficient quantity in stock.")
            return 0

    def update_quantity_in_csv(self):
        """Update the CSV file with the new book quantity."""
        path = "project1oop.csv"
        with open(path, "r", newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        # Find the row with the matching book title and update the quantity
        for row in rows:
            if row["title"].lower() == self.title.lower():
                row["quantity"] = str(self.quantity)

        # Write the updated data back to the CSV file
        with open(path, "w", newline='') as file:
            fieldnames = ["title", "author", "price", "isbn", "quantity"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    @classmethod
    def restock(cls, book_title: str):
        """Restock a specific book.

        Args:
            book_title (str): The title of the book to be restocked.
        """
        found_book = None
        for book_obj in cls.all_books:
            if book_obj.title.lower() == book_title.lower():
                found_book = book_obj
                break

        if found_book is None:
            print("Book not found.")
            return

        quantity_to_add = int(input("Enter the quantity to be added: "))
        found_book.quantity += quantity_to_add

        # Update the CSV file with the new quantity
        path = "project1oop.csv"
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        # Find the row with the matching book title and update the quantity
        for row in rows:
            if row["title"].lower() == book_title.lower():
                row["quantity"] = str(found_book.quantity)

        # Write the updated data back to the CSV file
        with open(path, "w", newline='') as file:
            fieldnames = ["title", "author", "price", "isbn", "quantity"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
