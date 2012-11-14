'''
Created on 16/10/2012

@author: mac
'''

from django.contrib.auth.models import User

from payment.services import access_customer_data

def customer_details(invoice_data):
    username = invoice_data['contract']
    
    # Adding customer details
    invoice_data['customer'] = load_user_profile(username)
    
    return invoice_data

def load_user_profile(username):
    users = User.objects.filter(username=username)
    
    if (len(users) != 1):
        print "Unknown user: " + username
        return {}
    
    user = users[0]

    return access_customer_data(user)
