from tabnanny import verbose
from unicodedata import name
from django.db import models

class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    class Meta:
        verbose_name ="Member"
        verbose_name_plural = "Members"

class ContactForm(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    message = models.CharField(max_length=1000)
