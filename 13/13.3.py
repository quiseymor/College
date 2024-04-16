import json

class Book:
    def __init__(self, title, author, year, quantity):
        self.title = title
        self.author = author
        self.year = year
        self.quantity = quantity

class BookDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.books = []

    def open_file(self):
        with open(self.filename, 'r') as file:
            self.books = json.load(file)

    def save_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.books, file, indent=4)

    def show_books(self):
        sorted_books = sorted(self.books, key=lambda x: x['author'])
        for book in sorted_books:
            print(json.dumps(book, indent=4))

    def add_book(self, title, author, year, quantity):
        new_book = {'title': title, 'author': author, 'year': year, 'quantity': quantity}
        self.books.append(new_book)

    def delete_book(self, title):
        self.books = [book for book in self.books if book['title'] != title]

    def edit_book(self, title, author, year, quantity):
        for book in self.books:
            if book['title'] == title:
                book['author'] = author
                book['year'] = year
                book['quantity'] = quantity

def main():
    db = BookDatabase('books.json')
    db.open_file()

    while True:
        print("\nMENU:")
        print("1. Show all books")
        print("2. Add a book")
        print("3. Delete a book")
        print("4. Edit a book")
        print("5. Save to file")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            db.show_books()
        elif choice == '2':
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = int(input("Enter year: "))
            quantity = int(input("Enter quantity: "))
            db.add_book(title, author, year, quantity)
        elif choice == '3':
            title = input("Enter title of the book to delete: ")
            db.delete_book(title)
        elif choice == '4':
            title = input("Enter title of the book to edit: ")
            author = input("Enter new author: ")
            year = int(input("Enter new year: "))
            quantity = int(input("Enter new quantity: "))
            db.edit_book(title, author, year, quantity)
        elif choice == '5':
            db.save_file()
            print("Data saved to file.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
