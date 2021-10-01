from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

# Create your views here.


def contact(request):
   
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            user_email = contact_form.cleaned_data['email_address']
            first_name = contact_form.cleaned_data['first_name']
            last_name = contact_form.cleaned_data['last_name']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            body = render_to_string(
                    'contact/emails/email_received_body.txt',
                    {'contact_email': settings.DEFAULT_FROM_EMAIL})

            send_mail(
                    subject,
                    body,
                    first_name,
                    last_name,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [user_email]
                )
                
            contact_form.save()
            messages.info(request, 'Message sent successfully !')
            return redirect(reverse('contact'))

        else:
            messages.error(request, 'There was a problem with your message. Please try again.')

    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
