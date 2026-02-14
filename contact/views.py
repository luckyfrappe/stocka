from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactMessageForm


def contact(request, user=None):
    """
    Renders the contact page and processes customer inquiry submissions.

    form: `ContactMessageForm`

    **context**:
    - `form`: instance of `ContactMessageForm` for user input

    template: `contact/contact.html`
    """
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your message has been sent successfully. '
                'We will get back to you as soon as possible.'
            )
            return redirect('contact')
        else:
            messages.error(
                request,
                'There was an error with your submission. Please '
                'check the form and try again or contact by email '
                'support@stocka.com.'
            )
    else:
        form = ContactMessageForm()

    if user.is_authenticated:
        user = request.user
        if user.email:
            form.fields['email'].initial = user.email
        if user.get_full_name():
            form.fields['name'].initial = user.get_full_name()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
