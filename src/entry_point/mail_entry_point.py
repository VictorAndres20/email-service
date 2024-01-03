from fastapi import APIRouter
from src.models.response import Response
from src.models.email_request import EmailRequest
from src.controller import email_controller

router = APIRouter(
    prefix="/send-email",
    responses={
        404: {"Description": "Not found"}
    }
)


@router.post("")
async def simple_email(body: EmailRequest) -> Response:
    return email_controller.send_basic_email(body)


@router.post("/bytes-att")
async def email_with_att(body: EmailRequest) -> Response:
    return email_controller.send_email_with_attachment(body)
