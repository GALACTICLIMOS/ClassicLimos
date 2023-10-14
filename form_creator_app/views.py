from django.conf import settings
from django.shortcuts import render
from django.core.mail import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
import os
import base64



def index(request):
    return render(request, 'index.html')