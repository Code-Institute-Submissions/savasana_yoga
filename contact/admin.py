from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):

    readonly_fields = (
        'first_name',
        'last_name',
        'email_address',
        'subject',
        'message',
        'sent'
    )

    list_display = (
        'subject',
        'first_name',
        'email_address',
        'sent'
    )

    ordering = ('-sent',)


admin.site.register(Contact, ContactAdmin)
