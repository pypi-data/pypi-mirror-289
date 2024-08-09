from django.core.mail import EmailMessage
from django.conf import settings
import logging


LOG = logging.getLogger()


def send_email(subject: str, message: str, recipients: list,
               attachment: any = None, attachment_name: str = '', attachment_type: any = '') -> int:

    try:
        mail = EmailMessage(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipients
        )

        if attachment:
            mail.attach(attachment_name, attachment, attachment_type)

        return mail.send()

    except Exception as e:
        LOG.error(f"ERRORE! {e}")
