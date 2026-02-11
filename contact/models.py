from django.db import models


class ContactMessage(models.Model):
    """
    Stores individual communication entries from the contact form.

    model: `ContactMessage`
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the message with status and
        timestamp.
        """
        return (
            f"{self.name} - {self.subject} - "
            f"{self.created_at.strftime('%Y-%m-%d %H:%M:%S')} - "
            f"{'Resolved' if self.is_resolved else 'Unresolved'}"
        )
