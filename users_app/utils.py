import secrets
from django.core.mail import send_mail
from django.conf import settings


def generate_confirmation_code():
    return secrets.token_urlsafe(16)


def send_confirmation_email(email, confirmation_code):
    subject = 'Подтверждение адреса электронной почты'
    message = f'Привет!\n\nПодтвердите ваш адрес электронной почты, перейдя по следующей ссылке: ' \
              f'http://127.0.0.1:8000/account/confirm-email/{confirmation_code}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
