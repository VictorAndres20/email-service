from src.models.email_request import EmailRequest
from src.models.response import Response, ResponseDictionary
from src.services.email_service import send_email, send_email_with_att


def send_basic_email(req: EmailRequest) -> Response:
    return rest_response(req, send_email)


def send_email_with_attachment(req: EmailRequest) -> Response:
    return rest_response(req, send_email_with_att)


def rest_response(req: EmailRequest, function) -> Response:
    code = 200
    ok = True
    msg = ''
    error = ''
    data_db = None
    try:
        data_db = function(req)
    except Exception as e:
        print(str(e))
        code = 500
        ok = False
        error = 'Ha ocurrido un error. ' + str(e)
    data = {'code': code, 'ok': ok, 'msg': msg, 'error': error, 'data': data_db}
    res = ResponseDictionary(**data)
    return res
