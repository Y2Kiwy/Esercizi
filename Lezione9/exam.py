# Exercise 1: ----------------------------------------------------------------
class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def symmetric(tree: list[int]) -> bool:
    # scrivere qui la vostra funzione
    pass
# ----------------------------------------------------------------------------

# Exercise 2: ----------------------------------------------------------------
def valid_sudoku(board: list[list[str]]) -> bool:
    # Rows validation
    for row_index in range(9):
        seen = set()
        for column_index in range(9):
            value = board[row_index][column_index]
            if value != ".":
                if value in seen:
                    print(f"Repetition in row {row_index}: {value}")
                    return False
                seen.add(value)
    
    # Columns validation
    for column_index in range(9):
        seen = set()
        for row_index in range(9):
            value = board[row_index][column_index]
            if value != ".":
                if value in seen:
                    print(f"Repetition in column {column_index}: {value}")
                    return False
                seen.add(value)
    
    # Subsection 3x3 validation
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            seen = set()
            for row_index in range(i, i + 3):
                for column_index in range(j, j + 3):
                    value = board[row_index][column_index]
                    if value != ".":
                        if value in seen:
                            print(f"Repetition in subsection ({i}-{j}): {value}")
                            return False
                        seen.add(value)
    
    return True

# ----------------------------------------------------------------------------



# Exercise 3: ----------------------------------------------------------------
class Account:
    
    def __init__(self, account_id: str, balance: float) -> None:
        self.account_id: str = account_id
        self.balance: float = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def get_balance(self) -> float:
        return self.balance

class Bank:

    def __init__(self) -> None:
        self.accounts: dict[str, Account] = {}

    def create_account(self, account_id: str) -> None:
        if account_id in self.accounts:
            raise ValueError("Account with this ID already exists")
        new_account: Account = Account(account_id, 0)
        self.accounts[new_account.account_id] = new_account
        return new_account

    def deposit(self, account_id: str, amount: float) -> None:
        self.accounts[account_id].deposit(amount)

    def get_balance(self, account_id: str) -> float:
        if not account_id in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_id].balance
# ----------------------------------------------------------------------------



# Exercise 4: ----------------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:

    # Initialize an empty list
    result = []

    # Create a pointer to the starting node
    current = head

    while current:

        # Insert the ListNode value at the start of the 'result' list
        result.insert(0, current.val)

        # Create a pointer to the next node
        current = current.next

    return result
# ----------------------------------------------------------------------------



# Exercise 5: ----------------------------------------------------------------
def anagram(s: str, t: str) -> bool:
    return True if sorted(s.lower()) == sorted(t.lower()) else False
# ----------------------------------------------------------------------------



# Exercise 6: ----------------------------------------------------------------
def word_break(s: str, wordDict: list[str]) -> bool:
    for word in wordDict:
        if word in s:
            print(f"Found {word} in {s}")
            s = s.replace(word, "")
            print(f"Updated 's' {s}")
        else:
            return False
        
    return True
# ----------------------------------------------------------------------------



# Exercise 7: ----------------------------------------------------------------
class Book:
    def __init__(self, book_id: str, title: str, author: str) -> None:
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = False

    def borrow(self) -> None:
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            raise ValueError("Book is already borrowed")

    def return_book(self) -> None:
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            raise ValueError("Book is not borrowed")


class Member:
    def __init__(self, member_id: str, name: str) -> None:
        self.member_id: str = member_id
        self.name: str = name
        self.borrowed_books: set[Book] = set()

    def borrow_book(self, book: Book) -> None:
        if not book in self.borrowed_books:
            book.borrow()
            self.borrowed_books.add(book)
        else:
            raise ValueError("Book is already borrowed")

    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            raise ValueError("Book not borrowed by this member")


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_id: str, title: str, author: str) -> None:
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author)

    def register_member(self, member_id: str, name: str) -> None:
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)

    def borrow_book(self, member_id: str, book_id: str) -> None:
        if member_id in self.members:
            if book_id in self.books:
                self.members[member_id].borrow_book(self.books[book_id])
            else:
                raise ValueError("Book not found")
        else:
            raise ValueError("Member not found")

    def return_book(self, member_id: str, book_id: str) -> None:
        if member_id in self.members:
            if book_id in self.books:
                self.members[member_id].return_book(self.books[book_id])
            else:
                raise ValueError("Book not found")
        else:
            raise ValueError("Member not found")

    def get_borrowed_books(self, member_id) -> list[Book]:
        if member_id in self.members:
            borrowed_books = self.members[member_id].borrowed_books
            return [book.title for book in borrowed_books]
# ----------------------------------------------------------------------------