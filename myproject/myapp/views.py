from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Contact
from .models import ContactForm
from django.template.loader import render_to_string
 
def index(request):
    return render(request, 'home.html', {})

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    print("hello")
    if request.method == 'POST':
        form = Contact(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            message = form.cleaned_data['Message']

            db_contactform = ContactForm()
            db_contactform.name = name
            db_contactform.email = email
            db_contactform.message = message
            db_contactform.save()

            html = render_to_string('emails/contactform.html',{
                'name' : name,
                'email' : email,
                'message' : message
            })
            send_mail('Contact Us - ' + name, 'The message','admin@nadia.com',['admin@nadia.com'], html_message=html)
            return redirect('/contact')
    else:
        form = Contact()

    return render(request, 'contact.html', {
        'form' : form
    })

def portfolio(request):
    return render(request, 'portfolio.html', {})
    