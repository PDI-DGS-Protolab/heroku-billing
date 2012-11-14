'''
Created on 06/11/2012

@author: mac
'''

from sforce.enterprise import SforceEnterpriseClient

SF_PRICELIST_ID = 'a13J0000000CtwvIAC'

SF_WSDL_PATH = 'resources/wsdl/salesforce-enterprise.wsdl'
SF_LOGIN     = 'agustin.martin@telefonica.com.dev'
SF_PWD       = 'chipotl6'
SF_TOKEN     = 'IVJeG9UJPc86xIY04jltqLoi'

#SF_WSDL_PATH = 'resources/wsdl/mac-salesforce-enterprise.wsdl'
#SF_LOGIN     = 'mac@telefonicadigital.es'
#SF_PWD       = 'tenderete13SA'
#SF_TOKEN     = 'zTlg3IiXhRQNqWN7mcxwF3LP'

def connect():
    c = SforceEnterpriseClient(SF_WSDL_PATH)
    c.login(SF_LOGIN, SF_PWD, SF_TOKEN)
    
    return c

def get_customers(account_id):
    
    c = connect()
    
    soql = """SELECT Email, Account.Name, Account.BillingCity, Account.BillingCountry, Account.BillingPostalCode, 
                     Account.BillingState, Account.BillingStreet 
              FROM   Contact 
              WHERE  AccountId='{0}'""".format(account_id)

    results = c.query(soql)
    
    if (results.size != 1):
        return (None. None)
    
    contact = results.records[0]
    account = contact.Account
    
    return (contact, account)

def get_catalogue():
    c = connect()
    
    soql = """SELECT Name, Price_per_Hour__c, Price_per_Month__c, Product_Code__c
              FROM Rate_Card_Item__c
              WHERE Rate_Card__c = '{0}'
            """.format(SF_PRICELIST_ID)

    results =  c.query(soql)
    
    catalogue = {}
    
    products = []
    
    for product in results.records:
        products.append({
                         'code'        : product.Product_Code__c, 
                         'description' : product.Name,
                         'price'       : product.Price_per_Hour__c
                         })
    
    catalogue['products'] = products
    
    return catalogue
