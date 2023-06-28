from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_mail(to_email, content):
    mail_subject = 'User information'
    message = render_to_string('management/mail-pattern.html', {'content': content})
    email = EmailMessage(
        mail_subject, message, to=to_email
    )
    email.send()
