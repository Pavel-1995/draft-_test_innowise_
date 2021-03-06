from django.core.mail import send_mail

from innowise.celery import app


@app.task
def send_email():
    """Send email about changes status"""
    send_mail(
        "status",
        "Status your ticket changed",
        "dudufhdbchfuhd@gmail.com",
        [
            "pavelalexei1177@gmail.com",
        ],
        fail_silently=False,
    )
