'''
Created on 16/10/2012

@author: mac
'''

from django.contrib.auth.models import User

from payment.services import accessCustomerData

def customerDetails(invoiceData):
    username = invoiceData['contract']
    
    # Adding customer details
    invoiceData['customer'] = loadUserProfile(username)
    
    return invoiceData

def loadUserProfile(username):
    users = User.objects.filter(username=username)
    
    if (len(users) != 1):
        print "Unknown user: " + username
        return {}
    
    user = users[0]

    return accessCustomerData(user)
