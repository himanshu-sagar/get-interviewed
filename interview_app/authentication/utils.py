import email
from django.core.mail import EmailMessage
from django.conf import settings
import os


class Util:
    @staticmethod
    def send_email(data):
        print(data)
        email = EmailMessage(data['email_subject'], data['body'], os.environ.get('EMAIL'), data['to_email'])
        email.send()
