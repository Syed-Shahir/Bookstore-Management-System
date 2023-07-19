import csv
#book class
class book:
    all_books = []
    def __init__(self,title:str,author:str,price:float,isbn:str,quantity:int):
        #initialize all the data
        self.title = title
        self.author = author
        self.price = price
        self.isbn = isbn
        self.quantity = quantity
        #storing data of all books
        book.all_books.append(self)
    #we will get details from csv file
    @classmethod
    def get_details(cls):
        book.all_books.clear()
        print("i am in get details")
        path = "project1oop.csv"
        with open(path, "r") as file:
            data = csv.DictReader(file)
            list_of_data = list(data)
        # Populate the all_books list with new book objects
        for value in list_of_data:
            book(value.get('title'), value.get('author'), float(value.get('price')), value.get('isbn'), int(value.get('quantity')))
    #this is to sell
    def sell_book(self,value):
        if value <= self.quantity:
            self.quantity -= value
            self.update_quantity_in_csv()
            return value * self.price
        else:
            print("Insufficient quantity in stock.")
            return 0
    def update_quantity_in_csv(self):
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
    #this is to restock
    @classmethod
    def restock(cls, booktitle: str):
        found_book = None
        for book_obj in cls.all_books:
            if book_obj.title.lower() == booktitle.lower():
                found_book = book_obj
                break

        if found_book is None:
            print("Book not found.")
            return

        q = int(input("Enter the quantity to be added: "))
        found_book.quantity += q

        # Update the CSV file with the new quantity
        path = "project1oop.csv"
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        # Find the row with the matching book title and update the quantity
        for row in rows:
            if row["title"].lower() == booktitle.lower():
                row["quantity"] = str(found_book.quantity)

        # Write the updated data back to the CSV file
        with open(path, "w", newline='') as file:
            fieldnames = ["title", "author", "price", "isbn", "quantity"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"Book '{found_book.title}' has been restocked by {q} units.")
#book class end

#customer class
class customer:
    customer_list = []
    def __init__(self,name,email,accbal):
        self.name = name
        self.email = email
        self.accbal = accbal
        customer.customer_list.append(self)
    @classmethod
    def customer_database(cls):
        customer.customer_list.clear()
        path = "project1custom.csv"
        with open (path,"r") as file:
            data = csv.DictReader(file)
            list_of_data = list(data)
        for value in list_of_data:
            customer(value.get('name'),value.get('email'),float(value.get('balance')))
    def purchase_book(self):
        total_bill = purchasing_book()
        print(f"your account balance is {self.accbal}")
        if total_bill > self.accbal:
            print("you have insufficient balance")
        else:
            self.accbal -= total_bill
            self.update_balance_in_csv()
            print("purchase successful")
    def update_balance_in_csv(self):
        path = "project1custom.csv"
        with open(path, "r", newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        # Find the row with the matching customer email and update the balance
        for row in rows:
            if row["email"].lower() == self.email.lower():
                row["balance"] = str(self.accbal)

        # Write the updated data back to the CSV file
        with open(path, "w", newline='') as file:
            fieldnames = ["name", "email", "balance"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

#customer class end

#bookstore class
class Bookstore:
    def __init__(self,list1:list,list2:list) :
        books_list = list1
        customer_data = list2
    
    def list_customers(self):
        customer.customer_list.clear()
        customer.customer_database()
        print(f"customer              |email          |  balance")
        for value in customer.customer_list:
            print(f"{value.name:20}  |{value.email:30}  |{value.accbal}")
        
    
    def list_books(self):
        book.get_details()
        print("****************MENU************************")
        print(f"Title       |  Author    |  Price|  ISBN      | Quantity")
        for value in book.all_books:
            print(f"{value.title:10}  |{value.author:10}  |{value.price:5}  |{value.isbn:10}  |{value.quantity:2}")
        
    def serch_book(self,bookname):
        for i in book.all_books:
            if i.title == bookname:
                print(f"this {bookname} is available details are as follows:")
                print(f"Title       |  Author    |  Price|  ISBN      | Quantity")
                print(f"{i.title:10}  |{i.author:10}  |{i.price:5}  |{i.isbn:10}  |{i.quantity:2}")
                break
            else:
                print("book is not available!!!")
    @classmethod
    def add_book(cls):
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
        path = "project1custom.csv"
        with open(path,"a",newline="") as file:
            writer = csv.writer(file)
            print("enter new account details:")
            name = input("enter your name = ")
            email = input("enter your email address = ")
            balance = float(input("enter your account balance = "))
            
            writer.writerow([name,email,balance])
#***********************************************************************

#functions
def purchasing_book():
    book.get_details()
    print("****************MENU************************")
    print(f"Title       |  Author    |  Price|  ISBN      | Quantity")
    for value in book.all_books:
        print(f"{value.title:10}  |{value.author:10}  |{value.price:5}  |{value.isbn:10}  |{value.quantity:2}")
    switch = True
    total_price = 0.0
    while switch:
        purchasing_book_title = input("Enter the title of the book (or 'exit' to stop): ").lower()

        if purchasing_book_title == "exit":
            switch = False
        else:
            found_book = None
            for book_obj in book.all_books:
                if book_obj.title.lower() == purchasing_book_title:
                    found_book = book_obj
                    break

            if found_book is None:
                print("Book not found. Please enter a valid book title.")
                continue

            quantity_to_buy = int(input("Enter the quantity to buy: "))
            if quantity_to_buy > found_book.quantity:
                print("Insufficient quantity in stock. Please enter a lower quantity.")
                continue

            total_price = total_price+found_book.sell_book(quantity_to_buy)
                
        if input("Do you want to buy more (y/n)? ").upper() == "N":
            return(total_price)
            switch = False

#main
book.get_details()
customer.customer_database()
store1 = Bookstore(book.all_books,customer.customer_list)



#********PORTAL***********
print("***HI!!!** WELCOME TO THE PORTAL MAIN PAGE***")
switch = True
while switch:
    login_option = input("are you admin or customer (exit)= ").lower()
    if login_option == "admin":
        print("choose from the following options :")
        print("press 1 to list all book details")
        print("press 2 to list all customer details")
        print("press 3 to add new book to the stock")
        print("press 4 to restock ")
        option = int(input("enter your option = "))
        if option == 1:
            store1.list_books()
        elif option == 2:
            store1.list_customers()
        elif option == 3:
            store1.add_book()
            book.get_details()
        elif option == 4:
            book.get_details()
            bookname = input("enter book name to restock = ").lower()
            book.restock(bookname)
        else:
            print("invalid option please try again!!!")         
            
    elif login_option == "customer":
        print("choose from the following options :")
        print("press 1 to list all available books")
        print("press 2 to register as new customer")
        print("press 3 to check for a specific book ")
        print("press 4 to purchase book if already a customer")
        option = int(input("enter your option = "))
        if option == 1:
            store1.list_books()
        elif option == 2:
            store1.add_customer()
            customer.customer_database()
        elif option == 3:
            b = input("enter the book name = ")
            store1.serch_book(b)
        elif option == 4:
            purchasing_book()
        else:
            print("invalid input please try again!!! ")
    elif login_option == "exit":
        switch = False
    else:
        print("invalid option")
