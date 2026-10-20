# src\routes\book_route.py
from fastapi import APIRouter
import rich
from src.model.book_table import Book
from src.model.user_table import User
from src.service.auth import verify_api_key
from src.utils.api_response import BookResponse
from fastapi.params import Depends
from sqlmodel import Session, select
from src.db.engine import get_session
from src.validator.user_validation import CreateUserRequest
from src.validator.book_validation import CreateBookRequest
from src.utils.exception import InvalidError



router = APIRouter(
    prefix="/book",
    tags=["book"],
)


# localhost:8000/book
@router.post("/", response_model=BookResponse)
async def create_book(book_data: CreateBookRequest, session: Session = Depends(get_session), api_key: str = Depends(verify_api_key)):
    """create a book into database"""

    book = Book(
        title =   book_data.title,
        author = book_data.author,
        price = book_data.price,
        is_sold = book_data.is_sold,
        user_id = book_data.user_id,
        condition = book_data.condition
    )

    # add user to database
    session.add(book)
    session.commit()
    session.refresh(book)

    return BookResponse(status="success", message="Book has been created", book=[book])




# localhost:8000/book
# localhost:8000/book?offset=0&limit=50
@router.get("/", response_model=BookResponse)
async def get_all_books( 
    title: str = None,
    offset: int = 0,
    limit: int = 10, 
    session: Session = Depends(get_session), 
    api_key: str = Depends(verify_api_key)):
    """get all books from database"""

    books = select(Book).filter(Book.is_sold == False)

    if title:
        books = books.where(Book.title.like(f"%{title}%"))

    query = books.offset(offset).limit(limit)
    result = session.exec(query) # to execute select query into database
    books = result.all()

    return BookResponse(status="success", message="Books have been fetched", book=books)



# localhost:8000/book/{id}
@router.patch("/{id}", response_model=BookResponse)
async def update_book(id: int, book_data: CreateBookRequest, session: Session = Depends(get_session), api_key: str = Depends(verify_api_key)):
    """update a book into database"""

    book = session.get(Book, id)

    if not book:
       raise InvalidError(error_status_code=404, reason="Book not found")

    book.title = book_data.title
    book.author = book_data.author
    book.price = book_data.price
    book.condition = book_data.condition
    book.is_sold = book_data.is_sold
    book.user_id = book_data.user_id

    session.add(book)
    session.commit()
    session.refresh(book)

    return BookResponse(status="success", message="Book has been updated", book=[book])





# localhost:8000/book/{id}
@router.delete("/{id}", response_model=BookResponse)
async def delete_book(id: int, session: Session = Depends(get_session), api_key: str = Depends(verify_api_key)):
    """delete a book from database"""

    book = session.get(Book, id)

    if not book:
       raise InvalidError(error_status_code=404, reason="Book not found")

    session.delete(book)
    session.commit()

    return BookResponse(status="success", message="Book has been deleted", book=[])




# single book get
# localhost:8000/book/{id}
@router.get("/{id}", response_model=BookResponse)
async def get_book(id: int, session: Session = Depends(get_session), api_key: str = Depends(verify_api_key)):
    """get a book from database"""

    book = session.get(Book, id)

    if not book:
       raise InvalidError(error_status_code=404, reason="Book not found")

    return BookResponse(status="success", message="Book has been fetched", book=[book])





# is_sold status update
@router.patch("/{id}/is_sold", response_model=BookResponse)
async def update_book_is_sold(id: int, is_sold: bool, session: Session = Depends(get_session), api_key: str = Depends(verify_api_key)):
    """update the is_sold status of a book"""

    book = session.get(Book, id)

    if not book:
       raise InvalidError(error_status_code=404, reason="Book not found")

    book.is_sold = is_sold

    session.add(book)
    session.commit()
    session.refresh(book)

    return BookResponse(status="success", message="Book is_sold status has been updated", book=[book])





# get all book fetch by user_id
@router.get("/user/{user_id}", response_model=BookResponse)
async def get_books_by_user_id(user_id: int, session: Session = Depends(get_session), api_key: str = Depends(verify_api_key)):
    """get all books by user_id"""

    books = session.query(Book).filter(Book.user_id == user_id).all()

    return BookResponse(status="success", message="Books have been fetched", book=books)