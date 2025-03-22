from models import db
from models import Author, Book, Chapter


def seed_data():
    authors = [
        Author(name="J.K. Rowling"),
        Author(name="George R.R. Martin"),
        Author(name="Agatha Christie")
    ]
    db.session.add_all(authors)
    db.session.commit()

    books = [
        Book(title="Harry Potter and the Philosopher's Stone", publication_year="1997", author_id=1),
        Book(title="A Game of Thrones", publication_year="1996", author_id=2),
        Book(title="Murder on the Orient Express", publication_year="1934", author_id=3)
    ]
    db.session.add_all(books)
    db.session.commit()

    chapters = [
        Chapter(title="The Boy Who Lived", page_count=15, book_id=1),
        Chapter(title="The Vanishing Glass", page_count=12, book_id=1),
        Chapter(title="Prologue", page_count=10, book_id=2)
    ]
    db.session.add_all(chapters)
    db.session.commit()
