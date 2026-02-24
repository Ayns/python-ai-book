# Library Management System - Chapter 7 Project

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrowed_by = None

    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by}"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        count = len(self.borrowed_books)
        return f"{self.name} (ID: {self.member_id}) - {count} book(s) borrowed"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Added: {book.title}")

    def add_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)
        print(f"Registered: {member.name}")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, isbn, member_id):
        book = self.find_book(isbn)
        member = self.find_member(member_id)

        if not book:
            print("Book not found.")
            return
        if not member:
            print("Member not found.")
            return
        if not book.is_available:
            print(f"'{book.title}' is already borrowed by {book.borrowed_by}.")
            return

        book.is_available = False
        book.borrowed_by = member.name
        member.borrowed_books.append(book)
        print(f"{member.name} borrowed '{book.title}'")

    def return_book(self, isbn, member_id):
        book = self.find_book(isbn)
        member = self.find_member(member_id)

        if not book or not member:
            print("Book or member not found.")
            return

        book.is_available = True
        book.borrowed_by = None
        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
        print(f"{member.name} returned '{book.title}'")

    def show_all_books(self):
        if not self.books:
            print("No books in library.")
            return
        for book in self.books:
            print(f"  {book}")

    def show_available_books(self):
        available = [b for b in self.books if b.is_available]
        if not available:
            print("No books available.")
            return
        for book in available:
            print(f"  {book}")

    def search_books(self, query):
        query = query.lower()
        results = [b for b in self.books
                   if query in b.title.lower() or query in b.author.lower()]
        if not results:
            print("No matches found.")
            return
        for book in results:
            print(f"  {book}")


# Main program
lib = Library("City Library")

# Add sample data
lib.add_book("Python Crash Course", "Eric Matthes", "978-1")
lib.add_book("Clean Code", "Robert Martin", "978-2")
lib.add_book("The Pragmatic Programmer", "David Thomas", "978-3")
lib.add_member("Alex", "M001")
lib.add_member("Mei", "M002")

print(f"\n{'=' * 40}")
print(f"  {lib.name.upper()}")
print(f"{'=' * 40}")

while True:
    print("\n1. Show All Books")
    print("2. Show Available Books")
    print("3. Search Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Show Members")
    print("7. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        lib.show_all_books()
    elif choice == "2":
        lib.show_available_books()
    elif choice == "3":
        query = input("Search: ")
        lib.search_books(query)
    elif choice == "4":
        isbn = input("Book ISBN: ")
        member_id = input("Member ID: ")
        lib.borrow_book(isbn, member_id)
    elif choice == "5":
        isbn = input("Book ISBN: ")
        member_id = input("Member ID: ")
        lib.return_book(isbn, member_id)
    elif choice == "6":
        for member in lib.members:
            print(f"  {member}")
    elif choice == "7":
        print("Goodbye!")
        break
