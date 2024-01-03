from src.entry_point import mail_entry_point
from fastapi import FastAPI


def set_api_routes(app: FastAPI):
    app.include_router(mail_entry_point.router)
