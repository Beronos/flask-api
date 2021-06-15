from models import Author
from extensions import db

def get_authors():
    return Author.query.all()


def get_author(author_id):
    return Author.query.filter_by(authorID=author_id).first()


def create_author(first_name, last_name):
    author = Author(FirstName=first_name, LastName=last_name)
    db.session.add(author)
    db.session.commit()
    return author


def update_author(author_id, first_name, last_name):
    author = get_author(author_id)
    author.FirstName = first_name
    author.LastName = last_name
    db.session.commit()
    return author


def delete_author(author_id):
    author = get_author(author_id)
    db.session.delete(author)
    db.session.commit()
    return author



