class Book:
    def __init__(self, book_id: str, title: str, author: str) -> None:
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = False



class Library:
    def __init__(self):
        self.catalog = []

    def add_book(self, book: Book) -> None:
        if book not in self.catalog:
            self.catalog.append(book)
            return f"{book.title} correctly added to library"

    def borrow_book(self, book_title: str) -> None:
        for book in self.catalog:
            if book_title == book.title:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    return f"{book.title} correctly borrowed: 'book.is_borrowed: {book.is_borrowed}'"
                else:
                    return f"Cannot borrow {book.title} it's already borrowed"
        return "Book do not exist"

    def return_book(self, book_title: str) -> None:
        for book in self.catalog:
            if book_title == book.title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    return f"{book.title} correctly returned: 'book.is_borrowed: {book.is_borrowed}'"
                else:
                    return f"Cannot return {book.title}, it's alerady returned"
        return "Book do not exist"
    
    def get_borrowed_books(self) -> list[str]:
        if self.catalog:
            return [book.title for book in self.catalog if not book.is_borrowed]
        else:
            raise RuntimeError ("There are no books in the library")



def main():
    # Creazione della libreria
    library = Library()

    # Aggiunta di alcuni libri all'inventario
    book1 = Book("001", "Harry Potter and the Philosopher's Stone", "J.K. Rowling")
    book2 = Book("002", "To Kill a Mockingbird", "Harper Lee")
    book3 = Book("003", "1984", "George Orwell")

    print(library.add_book(book1))
    print(library.add_book(book2))
    print(library.add_book(book3))

    # Prestito di un libro da parte di un utente
    print(library.borrow_book("To Kill a Mockingbird"))

    # Restituzione di un libro da parte di un utente
    print(library.return_book("To Kill a Mockingbird"))

    # Visualizzazione dei libri disponibili per il prestito
    try:
        available_books = library.get_borrowed_books()
        print("\nAvailable books for borrowing:")
        for book in available_books:
            print("- ", book)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()