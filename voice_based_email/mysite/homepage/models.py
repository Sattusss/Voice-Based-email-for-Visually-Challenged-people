from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class option(models.Model):
    option = models.CharField(max_length=100)

class Details:
    email : str
    password : str

class Compose:
    recipient : str
    subject : str
    body : str


class Mail(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_emails')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_emails')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    date = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('read', 'read'), ('unread', 'unread'), ('sent','sent')], default='unread')
    
    def __str__(self) -> str:
        return self.subject  
