
# 📚 Book Selling Platform

A web-based marketplace where users can list their used books for sale and browse books listed by other users. The platform helps students and readers buy and sell books conveniently.

## 🚀 Features
- User registration and authentication
- Add and manage book listings
- Browse books and view book details
- Book conditions, prices, and seller information
- Admin approval for new listings
- Responsive frontend with light and dark modes

## 🛠️ Tech Stack
- **Backend:** Python, FastAPI
- **Database & ORM:** SQLModel, SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript
- **Server:** Uvicorn
- **Version Control:** Git and GitHub

## 📂 Project Structure
- `main.py` — Application entry point
- `src/model/` — Database models
- `src/routes/` — API routes
- `src/service/` — Business logic and authentication
- `src/validator/` — Request validation
- `index.html` — Frontend interface

## ▶️ Getting Started

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the required dependencies.
4. Run the application:

```bash
uvicorn main:app --reload
```

5. Open `http://127.0.0.1:8000/docs` to explore the FastAPI API documentation.

## 🎯 Project Goal

To provide a simple and accessible platform for students and readers to buy and sell books, encourage book reuse, and make affordable reading materials available.
