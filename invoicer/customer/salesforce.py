'''
Created on 31/10/2012

@author: amg
'''

from sforce.enterprise import SforceEnterpriseClient

SF_WSDL_PATH = 'salesforce-enterprise.wsdl'
SF_LOGIN     = 'agustin.martin@telefonica.com.dev'
SF_PWD       = 'chipotl6'
SF_TOKEN     = 'IVJeG9UJPc86xIY04jltqLoi'

def connect():
    c = SforceEnterpriseClient(SF_WSDL_PATH)
    c.login(SF_LOGIN, SF_PWD, SF_TOKEN)
    
    return c

def getCustomerDetailsFromSalesForce(accountId):
    
    c = connect()
    
    soql = """SELECT Email, Account.Name, Account.BillingCity, Account.BillingCountry, Account.BillingPostalCode, 
                     Account.BillingState, Account.BillingStreet 
              FROM   Contact 
              WHERE  AccountId='{0}'""".format(accountId)

    result = c.query(soql)
    
    if (result.size != 1):
        return {}
    
    contact = result.records[0]
    account = contact.Account

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

def getCatalogue():
    
    c = connect()
    
    #soql = """SELECT Id, Name FROM Pricebook2"""
    soql = """SELECT Id FROM Price_List_Item__c"""

    result = c.query(soql)
    
    print result
    
    #print c.describeSObject('Product2')