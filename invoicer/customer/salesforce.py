'''
Created on 31/10/2012

@author: amg
'''

from common.salesforce.salesforce import get_customers

def get_customer_details_from_sf(account_id):
    
    (contact, account) = get_customers(account_id)
    
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

def customer_details_from_sf(invoice_json):
    account_id = invoice_json['contract']
    
    # Adding customer details
    invoice_json['customer'] = get_customer_details_from_sf(account_id)
    
    return invoice_json