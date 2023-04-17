# views.py

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import Email


def index(request):
    return render(request, 'index.html')


def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = request.POST.get('from_email')
        recipient_list = request.POST.get('recipient_list')

        # Save email data to database
        email = Email(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)


        # Use your email as the recipient
        to_email_list = [settings.DEFAULT_TO_EMAIL]

        # Send email
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )

        return HttpResponse('Email sent successfully and data saved to database')
    return render(request, 'email_form.html')