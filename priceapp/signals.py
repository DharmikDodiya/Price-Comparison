from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.conf import settings

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = "Welcome to Price Comparison"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [instance.email]

        # Generate the HTML content
        html_content = render_to_string('emails/welcome_email.html', {'user': instance})

        # Create the email message
        email = EmailMultiAlternatives(subject, html_content, from_email, to_email)
        email.attach_alternative(html_content, "text/html")
        email.send()
