#!/usr/bin/python
#coding=utf-8 

"""
Copyright 2012 Telefonica Investigación y Desarrollo, S.A.U

This file is part of Billing_PoC.

Billing_PoC is free software: you can redistribute it and/or modify it under the terms 
of the GNU Affero General Public License as published by the Free Software Foundation, either 
version 3 of the License, or (at your option) any later version.
Billing_PoC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even 
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero 
General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with Billing_PoC. 
If not, see http://www.gnu.org/licenses/.

For those usages not covered by the GNU Affero General Public License please contact with::mac@tid.es
"""  

'''
Created on 30/10/2012

@author: mac@tid.es
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
