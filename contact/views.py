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
        user_message = request.POST.get('message')
        subject = request.POST.get('subject')
        user_email = request.POST.get('user_email')

        if contact_form.is_valid():
            user_email = contact_form.cleaned_data['email_address']
            subject = contact_form.cleaned_data['subject']
            body = render_to_string(
                'contact/emails/email_received_body.txt',
                {'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [user_email]
            )

            contact_form.save()
            messages.success(request, 'Message sent successfully !')
            return redirect(reverse('contact'))

        else:
            messages.error(request, 'There was a problem with your message. Please try again.')

    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request):

    return render(request, 'contact/contact_success.html')
