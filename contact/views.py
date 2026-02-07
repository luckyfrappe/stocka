from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from .models import ContactMessage
from django.contrib import messages

# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            messages.success(request, 'Your message has been sent successfully. We will get back to you as soon as possible.')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again or contact by email support@stocka.com.')
    else:
        form = ContactMessageForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'contact/contact.html', context)