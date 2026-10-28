# Aggregation (Weak Has-a)

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, books):
        # Library receives books that already exist
        self.books = books

# Run
book1 = Book("The Hobbit")
book2 = Book("1984")

my_library = Library([book1, book2])

print("Books in library:")
for book in my_library.books:
    print("-", book.title)
