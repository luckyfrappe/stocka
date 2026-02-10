from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        Connects signal receivers when the app is ready.
        """
        import checkout.signals  # noqa
