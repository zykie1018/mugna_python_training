class Library:
    # Class variable
    books = []

    def __init__(self, name):
        # instance variables
        self.name = name

    def add_books(self, book):
        self.books.append(book)

    def remove_books(self, book):
        self.books.pop(book)


def main():
    library_1 = Library(name="Public Library")
    library_2 = Library(name="Private Library")

    library_1.add_books("Hello World 101")
    library_2.add_books("Ds ALgo")

    # library_1.remove_books(1)
    y = library_2.name
    print(y)
    x = library_1.books
    print(x)


if __name__ == '__main__':
    main()