# Exercise 1 -----------------------------------------------------------------

class Movie:
    def __init__(self, movie_id: str, title: str, director: str) -> None:
        self.movie_id: str = movie_id
        self.title: str = title
        self.director: str = director

        self.is_rented: bool = False

    def rent(self) -> None:
        """Rent the movie if it's possible to"""
        if not self.is_rented:
            self.is_rented = True
        else:
            print(f"Il film '{self.title}' è già stato noleggiato.")

    def return_movie(self) -> None:
        """Return and free the movie"""
        if self.is_rented:
            self.is_rented = False
        else:
            print(f"Il film {self.title} non è attualmente noleggiato.")

class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id: str = customer_id
        self.name: str = name

        self.rented_movies: list[Movie] = list()

    def rent_movie(self, movie: Movie) -> None:
        """Rent the movie if it's possible"""
        if not movie.is_rented:
            movie.rent()
            self.rented_movies.append(movie)
        else:
            print(f"Il film '{movie.title}' è già noleggiato.")

    def return_movie(self, movie: Movie) -> None:
        """Return the movie if it's been rented by the user"""
        if movie in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)
        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")

class VideoRentalStore:
    def __init__(self) -> None:
        self.movies: dict[str, Movie] = dict()
        self.customers: dict[str, Customer] = dict()

    def add_movie(self, movie_id: str, title: str, director: str) -> None:
        """Add movie to movies dict if it's not already there"""
        to_add_movie: Movie = Movie(movie_id, title, director)

        if not movie_id in self.movies:
            self.movies[movie_id] = to_add_movie
        else:
            print(f"Il film con ID {movie_id} esiste già.")

    def register_customer(self, customer_id: str, name: str) -> None:
        """Add movie to movies dict if it's not already there"""
        to_add_customer: Customer = Customer(customer_id, name)

        if not customer_id in self.customers:
            self.customers[customer_id] = to_add_customer
        else:
            print(f"Il cliente con ID {customer_id} è già registrato.")

    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        """Allow an existing customer to rent an existing movie"""
        if customer_id in self.customers and movie_id in self.movies:

            customer: Customer = self.customers[customer_id]
            movie: Movie = self.movies[movie_id]

            customer.rent_movie(movie)

        else:
            print("Cliente o film non trovato.")

    def return_movie(self, customer_id: str, movie_id: str) -> None:
        """Allow an existing customer to return an existing movie"""
        if customer_id in self.customers and movie_id in self.movies:

            customer: Customer = self.customers[customer_id]
            movie: Movie = self.movies[movie_id]

            customer.return_movie(movie)

        else:
            print("Cliente o film non trovato.")

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        else:
            print("Cliente non trovato.")
            return list()

# ----------------------------------------------------------------------------




# Exercise 5 -----------------------------------------------------------------

class Account:
    def __init__(self, account_id: str, balance: float) -> None:
        self.account_id: str = account_id
        self.balance: float = balance

    def deposit(self, amount: float) -> None:
        """Add the amount to the account balance"""
        self.balance += amount

    def get_balance(self) -> float:
        """Return the account balance"""
        return self.balance

class Bank:
    def __init__(self) -> None:
        self.accounts: dict[str, Account] = dict()

    def create_account(self, account_id) -> None:
        """Create new account"""
        if not account_id in self.accounts:
            new_account: Account = Account(account_id, 0.0)
            self.accounts[account_id] = new_account
            return new_account
        else:
            raise ValueError("Account with this ID already exists")

    def deposit(self, account_id: str, amount: float) -> None:
        """Deposit specific amount to a specific acount"""
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount)
        else:
            raise ValueError("Account not found")

    def get_balance(self, account_id) -> float:
        """Return the balance of a scpecific account"""
        if account_id in self.accounts:
            return self.accounts[account_id].get_balance()
        else:
            raise ValueError("Account not found")

# ----------------------------------------------------------------------------



# Exercise 7 -----------------------------------------------------------------

class Book:
    def __init__(self, book_id: str, title: str, author: str) -> None:
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = False

    def borrow(self) -> None:
        """Borrow the book"""
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            raise ValueError("Book is already borrowed")

    def return_book(self) -> None:
        """Return the book"""
        if self.is_borrowed:
            self.is_borrowed = False

class Member:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id: str = member_id
        self.name: str = name

        self.borrowed_books: list[Book] = list()

    def borrow_book(self, book: Book) -> None:
        """Mark a book as borrowed if possible and
        add the book to member borrowed books list"""
        book.borrow()
        if book.is_borrowed:
            self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        """Mark a book as free if possible and
        remove the book to member borrowed books list"""
        book.return_book()
        if not book.is_borrowed:
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)
            else:
                raise ValueError("Book not borrowed by this member")
class Library:
    def __init__(self) -> None:
        self.books: dict[str, Book] = dict()
        self.members: dict[str, Member] = dict()

    def add_book(self, book_id: str, title: str, author: str) -> None:
        """Add book to library books list"""
        book: Book = Book(book_id, title, author)

        if book_id not in self.books:
             self.books[book_id] = book

    def register_member(self, member_id:str, name: str) -> None:
        """Add member to library members list"""
        member: Member = Member(member_id, name)

        if member not in self.members:
             self.members[member_id] = member

    def borrow_book(self, member_id: str, book_id: str) -> None:
        """Borrow specific book as specific member"""
        if member_id in self.members:
            member: Member = self.members[member_id]
        else:
            raise ValueError("Member not found")
        
        if book_id in self.books:
            book: Book = self.books[book_id]
        else:
            raise ValueError("Book not found")

        member.borrow_book(book)

    def return_book(self, member_id: str, book_id: str) -> None:
        """Return specific book as specific member"""
        member: Member = self.members[member_id]
        book: Book = self.books[book_id]

        member.return_book(book)

    def get_borrowed_books(self, member_id) -> list[Book]:
        """Return the names of the book borrowed by specific member"""
        borrowed_names: list[str] = list()
        for book in self.members[member_id].borrowed_books:
            borrowed_names.append(book.title)
        return borrowed_names

# ----------------------------------------------------------------------------
