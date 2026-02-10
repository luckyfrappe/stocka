from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    """
    Form for capturing customer inquiries and support requests.

    model: `ContactMessage`
    Used in the contact view to facilitate communication between users and the business.
    """
    class Meta:
        model = ContactMessage
        exclude = ('user', 'created_at', 'is_resolved')

    def __init__(self, *args, **kwargs):
        """
        Initializes the form with custom placeholders and CSS classes.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False
