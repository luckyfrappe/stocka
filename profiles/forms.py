from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for users to update their profile information and delivery preferences.

    model: `UserProfile`
    Used in the profile view to manage default shipping details.
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Initializes the form with custom placeholders, CSS classes, and field styling.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country' and field != 'marketing_opt_in':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'

            if field != 'marketing_opt_in':
                self.fields[field].label = False
            else:
                self.fields[field].widget.attrs['class'] = 'form-check-input'
                self.fields[field].label = 'Subscribe to our newsletter'
