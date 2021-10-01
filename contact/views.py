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
            subject = (" Message Received: " + contact_form.cleaned_data['subject'])
            body = render_to_string(
                'contact/emails//email_received_body.txt',
                {'contact_email': settings.DEFAULT_FROM_EMAIL})

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [user_email]
            )

            if settings.EMAIL_HOST_USER:
                admin_email = settings.EMAIL_HOST_USER
            else:
                admin_email = settings.DEFAULT_FROM_EMAIL

            first_name = contact_form.cleaned_data['first_name']
            last_name = contact_form.cleaned_data['last_name']
            message = contact_form.cleaned_data['message']
            admin_body = render_to_string(
                'contact/emails/admin_email.txt',
                {
                    'sender_email': user_email,
                    'first_name': first_name,
                    'last_name': last_name,
                    'subject': subject,
                    'message': message,
                })

            send_mail(
                subject,
                admin_body,
                settings.DEFAULT_FROM_EMAIL,
                [admin_email]
            )

            contact_form.save()
            messages.info(request, 'Message sent successfully !')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'There was a problem with your message. Please try again.')

    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }
    
    return render(request, template, context)
