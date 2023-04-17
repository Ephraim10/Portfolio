# models.py

from django.db import models

class Email(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    from_email = models.EmailField()
    recipient_list = models.EmailField()
