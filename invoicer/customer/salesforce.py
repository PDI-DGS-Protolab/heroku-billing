'''
Created on 31/10/2012

@author: amg
'''

from common.salesforce.salesforce import getCustomers

def getCustomerDetailsFromSalesForce(accountId):
    
    (contact, account) = getCustomers(accountId)
    
    if contact == None:
        return {}

    return {
            'name'       : account.Name, 
            'address'    : account.BillingStreet, 
            'city'       : account.BillingCity, 
            'postal_code': account.BillingPostalCode, 
            'email'      : contact.Email,
            'country'    : account.BillingCountry,
            'order'      : 'f4f5e91595'
    }

def customerDetailsFromSF(invoiceJson):
    accountId = invoiceJson['contract']
    
    # Adding customer details
    invoiceJson['customer'] = getCustomerDetailsFromSalesForce(accountId)
    
    return invoiceJson