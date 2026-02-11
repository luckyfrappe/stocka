import time
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Order
from profiles.models import UserProfile


class StripeWH_Handler:
    """
    Handles Stripe webhook events to ensure database integrity and
    communication.

    Listens for asynchronous notifications from Stripe to verify
    transactions independently of the client-side checkout view.
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Sends a transactional confirmation email to the customer.

        **context**:
        - `order`: instance of model `Order` used for template data
        """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handles generic or unexpected Stripe webhook events.
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Verifies the order and updates user profile data upon successful
        payment.

        model: `Order`, `UserProfile`
        """
        # Get the payment intent data from the event
        intent = event.data.object
        pid = intent.id
        save_info = intent.metadata.save_info

        shipping_details = intent.shipping

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.get('username')

        if username and username != 'AnonymousUser':
            try:
                profile = UserProfile.objects.get(user__username=username)
                if save_info:
                    profile.default_phone_number = (
                        shipping_details.phone
                    )
                    profile.default_country = (
                        shipping_details.address.country
                    )
                    profile.default_postcode = (
                        shipping_details.address.postal_code
                    )
                    profile.default_town_or_city = (
                        shipping_details.address.city
                    )
                    profile.default_street_address1 = (
                        shipping_details.address.line1
                    )
                    profile.default_street_address2 = (
                        shipping_details.address.line2
                    )
                    profile.default_county = (
                        shipping_details.address.state
                    )
                    profile.save()
            except UserProfile.DoesNotExist:
                profile = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                # The Handshake.
                order = Order.objects.get(stripe_pid=pid)
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            # Mark the order as payment confirmed
            order.payment_confirmed = True
            order.save()

            self._send_confirmation_email(order)
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} | '
                    f'SUCCESS: Verified order already in database',
                ),
                status=200)
        else:
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} | '
                    f'ERROR: Order not found in DB. Handshake failed.',
                ),
                status=500)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handles failed payment intent notifications from Stripe.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
