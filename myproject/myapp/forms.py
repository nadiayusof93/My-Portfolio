from dataclasses import field
from django import forms

class ContactForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    Message = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

class Contact(forms.Form):
    class Meta:
        model = ContactForm
        field = ['name','email','message']