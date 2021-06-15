from models import Book
from extensions import db
from controllers import author_controller


def get_books():
    return Book.query.all()


def get_book(isbn):
    return Book.query.filter_by(ISBN=isbn).first()


def create_book(book_input):
    book = Book(Title=book_input.title, PublicationYear=book_input.publicationYear, Stock=book_input.stock,
                Rating=book_input.rating, Description=book_input.description, Genre=book_input.genre,
                IMGLocation=book_input.IMGLocation)
    for author_id in book_input.authors_id:
        book.authors.append(author_controller.get_author(author_id))
    db.session.add(book)
    db.session.commit()
    return book


def update_book(book_isbn, book_input):
    book = get_book(book_isbn)
    book.Title = book_input.title
    book.PublicationYear = book_input.publicationYear
    book.Stock = book_input.stock
    book.Rating = book_input.rating
    book.Description = book_input.description
    book.Genre = book_input.genre
    book.IMGLocation = book_input.IMGLocation
    if len(book_input.authors_id) > 0:
        book.authors = []
        for author_id in book_input.authors_id:
            book.authors.append(author_controller.get_author(author_id))
    db.session.commit()
    return book


def delete_book(book_isbn):
    book = get_book(book_isbn)
    db.session.delete(book)
    db.session.commit()
    return book


def get_total_stock():
    sum = 0
    books = get_books()
    for book in books:
        sum += book.Stock
    return sum



