from fastapi import FastAPI, APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_303_SEE_OTHER

app = FastAPI()
router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", name="index")
async def home(request: Request):
    return templates.TemplateResponse("index2.html", {"request": request})


@router.get("/login", name="login")
async def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login", name="login_post")
async def login_post(
    request: Request, username: str = Form(...), password: str = Form(...)
):
    if username == "testuser" and password == "testpass":
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    return templates.TemplateResponse(
        "login.html", {"request": request, "error": "Invalid credentials"}
    )


@router.get("/register")
async def register_get(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
async def register_post(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    password_confirm: str = Form(...),
):
    if password != password_confirm:
        return templates.TemplateResponse(
            "register.html", {"request": request, "error": "Passwords do not match"}
        )
    return RedirectResponse(url="/login", status_code=HTTP_303_SEE_OTHER)


app.include_router(router)
