from extensions import db
from sqlalchemy.orm import relationship, backref
import hashlib

class Author(db.Model):
    __tablename__ = "author"

    authorID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.Text)
    LastName = db.Column(db.Text)

    books = relationship("Book", secondary="authorbook", lazy='select')

    def __repr__(self):
        return f"<Author {self.FirstName} {self.LastName}>"


class Book(db.Model):
    __tablename__ = "book"

    ISBN = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.Text)
    PublicationYear = db.Column(db.Text)
    Stock = db.Column(db.SmallInteger)
    Rating = db.Column(db.DECIMAL)
    Description = db.Column(db.Text)
    Genre = db.Column(db.String)
    IMGLocation = db.Column(db.String)

    authors = relationship("Author", secondary="authorbook", lazy='select')
    users = relationship("User", secondary="loan", lazy='select')

    def __repr__(self):
        return f"<Book {self.Title}>"


class AuthorBook(db.Model):
    __tablename__ = 'authorbook'

    ab_id = db.Column(db.Integer, primary_key=True)
    bookISBN = db.Column(db.Integer, db.ForeignKey('book.ISBN'))
    authorID = db.Column(db.Integer, db.ForeignKey('author.authorID'))

    book = relationship(Book, backref=backref("book", cascade="all, delete-orphan"))
    author = relationship(Author, backref=backref("author", cascade="all, delete-orphan"))


class User(db.Model):
    __tablename__ = 'user'

    UserName = db.Column(db.String(), primary_key=True, nullable=False)
    Password = db.Column(db.String(), nullable=False)
    isAdmin = db.Column(db.Boolean(), nullable=False)

    books = relationship("Book", secondary="loan", lazy='select')

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(UserName=username).first()

    def check_password(self, password):
        return self.Password == hashlib.md5(password.encode()).hexdigest()

    def __repr__(self):
        return f"<User {self.UserName}>"


class Loan(db.Model):
    __tablename__ = 'loan'

    loanID = db.Column(db.Integer, primary_key=True)
    ISBN = db.Column(db.Integer, db.ForeignKey('book.ISBN'))
    username = db.Column(db.Integer, db.ForeignKey('user.UserName'))

    loaned_book = relationship(Book, backref=backref("loaned_book", cascade="all, delete-orphan"))
    user = relationship(User, backref=backref("user", cascade="all, delete-orphan"))




