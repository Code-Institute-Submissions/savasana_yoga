from django.db import models

# Create your models here.


class Contact(models.Model):
    """Saves a contact model in database."""

    class Meta:
        verbose_name_plural = 'Contact Forms'

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email_address = models.EmailField(max_length=250)
    subject = models.CharField(max_length=60)
    message = models.TextField(max_length=1500)
    sent = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
