'''
Created on 30/10/2012

@author: mac
'''

from django.core.mail import EmailMessage

def sendEmail(json):
    customerEmail = json['customer']['email']
    file_name     = json['pdf_file_name']
    
    emailMessage = EmailMessage('Hello', 'Body goes here', 'macvaz82@gmail.com',
                                [customerEmail], [], headers = {})
    
    emailMessage.attach_file(file_name, 'application/pdf')
    
    emailMessage.send(fail_silently=True)
