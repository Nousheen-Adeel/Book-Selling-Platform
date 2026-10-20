# main.py
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from src.db.engine import create_tables
from src.routes.user_route import router as user_router
from src.routes.book_route import router as book_router
from src.utils.exception import InvalidError, invalid_error_handler # pyright: ignore[reportMissingImports]
from src.model.user_table import User
from src.model.book_table import Book

User.model_rebuild()
Book.model_rebuild()

# control you starting and ending of server
@asynccontextmanager
async def lifespan(params: FastAPI):
    print("✅ server start ho gaya")
    create_tables()
    yield
    print("❌ server stop ho gaya")

app = FastAPI(
    title="Book selling backend Api",
    description="This is a backend api for book selling",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception class register in fastApi
app.add_exception_handler(InvalidError, invalid_error_handler)

app.include_router(user_router)
app.include_router(book_router)

@app.get("/")
def hello():
    index_path = Path(__file__).parent / "index.html"
    if index_path.exists():
        return FileResponse(index_path)
    return {"message" : "hello i am here!"}