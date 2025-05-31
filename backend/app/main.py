from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import sqlite3
from passlib.context import CryptContext


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Zgubka backend is alive"}


# # Initialize FastAPI and Jinja2 templating engine
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# # Password hashing setup
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# # SQLite database connection
# def get_db_connection():
#     conn = sqlite3.connect("zgubka.db")
#     conn.row_factory = sqlite3.Row
#     return conn


# # Home page route
# @app.get("/", response_class=HTMLResponse)
# async def read_home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


# # Add item form route (POST)
# @app.post("/add_item/")
# async def add_item(
#     request: Request,
#     name: str = Form(...),
#     description: str = Form(...),
#     category: str = Form(...),
#     location: str = Form(...),
#     photo_url: str = Form(...),  # Placeholder for photo URL field
# ):
#     conn = get_db_connection()
#     conn.execute(
#         "INSERT INTO items (name, description, category, location, photo_url, status) VALUES (?, ?, ?, ?, ?, ?)",
#         (
#             name,
#             description,
#             category,
#             location,
#             photo_url,
#             "lost",
#         ),  # Assuming default "lost"
#     )
#     conn.commit()
#     conn.close()
#     return templates.TemplateResponse(
#         "index.html", {"request": request, "message": "Item added successfully!"}
#     )


# # Example of user registration
# class UserCreate(BaseModel):
#     username: str
#     email: str
#     password: str


# @app.post("/register/")
# async def register_user(user: UserCreate):
#     hashed_password = pwd_context.hash(user.password)
#     conn = get_db_connection()
#     conn.execute(
#         "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
#         (user.username, user.email, hashed_password),
#     )
#     conn.commit()
#     conn.close()
#     return {"message": "User registered successfully!"}
