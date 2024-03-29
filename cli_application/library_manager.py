from models import Book, User, Loan

class LibraryManager:
    def list_books(self):
        books = Book.query.all()
        for book in books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}")

    def borrow_book(self, book_id):
        user_id = 1  # Assuming user ID 1 for simplicity
        book = Book.query.get(book_id)
        if book:
            loan = Loan(user_id=user_id, book_id=book_id)
            loan.save()
            print(f"Book '{book.title}' borrowed successfully!")
        else:
            print("Book not found.")

