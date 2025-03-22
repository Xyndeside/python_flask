import asyncio
from database import engine, async_session, Base
from models import Author, Book, Chapter


async def init_db(drop_tables=False):
    if drop_tables:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    authors_data = [
        {"name": "J.K. Rowling"},
        {"name": "George R.R. Martin"},
        {"name": "Agatha Christie"}
    ]

    books_data = [
        {"title": "Harry Potter and the Philosopher's Stone", "publication_year": "1997", "author_id": 1},
        {"title": "A Game of Thrones", "publication_year": "1996", "author_id": 2},
        {"title": "Murder on the Orient Express", "publication_year": "1934", "author_id": 3}
    ]

    chapters_data = [
        {"title": "The Boy Who Lived", "page_count": 15, "book_id": 1},
        {"title": "The Vanishing Glass", "page_count": 12, "book_id": 1},
        {"title": "Prologue", "page_count": 10, "book_id": 2}
    ]

    async with async_session() as session:
        for author in authors_data:
            author = Author(**author)
            session.add(author)

        for book in books_data:
            book = Book(**book)
            session.add(book)

        for chapter in chapters_data:
            chapter = Chapter(**chapter)
            session.add(chapter)

        await session.commit()

if __name__ == '__main__':
    asyncio.run(init_db())