from src.models.email_request import EmailRequest
from src.services.mail.mime_message import build_att_dict
from src.services.mail.smtp_sender import SMTPSender
from email.mime.base import MIMEBase
from src.utils.gen_file_by_bytes64 import build_file, FOLDER_PDF
from dotenv import dotenv_values
config = dotenv_values(".env")

host = config["EMAIL_HOST"]
port = config["EMAIL_PORT"]
user = config["EMAIL_USER"]
password = config["EMAIL_PASSWORD"]
name_from = config["EMAIL_NAME"]


def send_email(req: EmailRequest):
    smtp = SMTPSender(host, int(port if port != None else 0), user, password, name_from)
    recipients = [req.email]
    smtp.send_mail(recipients, req.subject, req.message, req.name)


def send_email_with_att(req: EmailRequest):
    if req.bytes == None:
        raise Exception('Bytes are null')
    pdf_filename = build_file(req.bytes, 'pdf')
    smtp = SMTPSender(host, port, user, password, name_from)
    recipients = [req.email]
    pdf_mime_base = MIMEBase("application", "pdf")
    attachment_list = [build_att_dict(pdf_mime_base, FOLDER_PDF, pdf_filename, att_name="respuestas.pdf")]
    smtp.send_mail(recipients, req.subject, req.message, req.name, attachment_list=attachment_list)
