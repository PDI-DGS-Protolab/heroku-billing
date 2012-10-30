'''
Created on 16/10/2012

@author: mac
'''

import urllib2
import json

URL = "http://10.95.193.53:8080/customers/{0}/data"

from django.contrib.auth.models import User

from payment.services import accessCustomerData

def customerDetails(invoiceData):
    username = invoiceData['contract']
    
    # Adding customer details
    #invoiceData['customer'] = downloadUserProfile(username)
    invoiceData['customer'] = loadUserProfile(username)
    
    return invoiceData

def downloadUserProfile(username):
    url      = URL.format(username)
    
    response = urllib2.urlopen(url)
    customer_details = response.read()
    
    return json.loads(customer_details)

def loadUserProfile(username):
    users = User.objects.filter(username=username)
    
    if (len(users) != 1):
        print "Unknown user: " + username
        return {}
    
    user = users[0]

    return accessCustomerData(user)
