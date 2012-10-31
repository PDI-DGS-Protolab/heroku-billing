'''
Created on 30/10/2012

@author: mac
'''

from django.core.mail import EmailMessage
from common.aws.constants import EMAIL_FROM, EMAIL_TITLE, EMAIL_BODY

def sendEmail(json):
    customerEmail = json['customer']['email']
    file_name     = json['pdf_file_name']
    
    emailMessage = EmailMessage(EMAIL_TITLE, EMAIL_BODY, EMAIL_FROM,
                                [customerEmail], [], headers = {})
    
    emailMessage.attach_file(file_name, 'application/pdf')
    
    emailMessage.send(fail_silently=True)
    
    return json
