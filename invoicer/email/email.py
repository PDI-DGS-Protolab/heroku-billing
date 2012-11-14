'''
Created on 30/10/2012

@author: mac
'''

from django.core.mail import EmailMessage
from common.aws.constants import EMAIL_FROM, EMAIL_TITLE, EMAIL_BODY

def send_email(json):
    customer_email = json['customer']['email']
    file_name      = json['pdf_file_name']
    
    email_message = EmailMessage(EMAIL_TITLE, EMAIL_BODY, EMAIL_FROM,
                                 [customer_email], [], headers = {})
    
    email_message.attach_file(file_name, 'application/pdf')
    
    email_message.send(fail_silently=True)
    
    return json
