from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import Subscriber, Campaign
import smtplib
from email.mime.multipart import MIMEMultipart




def add_subscriber(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        subscriber = Subscriber(email=email, first_name=first_name)
        subscriber.save()
        return HttpResponse('Successfully subscribed.')
    return render(request, 'add_subscriber.html')


def unsubscribe(request, subscriber_id):
    subscriber = Subscriber.objects.get(pk=subscriber_id)
    subscriber.is_active = False
    subscriber.save()
    return HttpResponse('Successfully unsubscribed.')

def send_daily_campaigns(request):
    subscribers = Subscriber.objects.filter(is_active=True)
    campaigns = Campaign.objects.all()
    for campaign in campaigns:
        for subscriber in subscribers:
            # Use campaign details and subscriber information to render the email content
            html_content = render_to_string('campaign_email.html', {
                'campaign': campaign,
                'subscriber': subscriber,
            })
        


        # Send email using SMTP
        send_email_smtp(subscriber.email, campaign.subject, html_content)
        return render(request, 'send_daily_campaign.html')
    return HttpResponse('Campaigns sent successfully.')



def send_email_smtp(subscriber_email, subject, html_content):
    # Configure your SMTP server and credentials
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'samplemailid@gmail.com'
    smtp_password = '@Password'
    sender_email = 'samplemailid@gmail.com'
    subscribers = ['subscriber1@example.com', 'subscriber2@example.com']

    base_template = 'campaign_email.html'  # Path to your base email template
    context = {
        'campaign': {
            'subject': subject,
            'preview_text': preview_text,
            'article_url': article_url,
            'html_content': html_content,
            'plain_text_content': plain_text_content,
            'published_date': published_date,
        }
    }
    email_content = render_to_string(base_template, context)

    # Send the campaign email to each subscriber
    for subscriber_email in subscribers:
        # Create the email message
        message = MIMEMultipart('alternative')
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = subscriber_email


    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('samplemailid@gmail.com', '@Password')
        server.sendmail(smtp_username, subscriber_email, message)

        

            
    



