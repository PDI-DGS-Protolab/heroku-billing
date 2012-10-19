#!/usr/bin/python
# coding=utf-8 

'''
Created on 10/10/2012

@author: mac
'''

from constants import CATALOGUE, TAX
from BeautifulSoup import BeautifulSoup

def parseSDR(xml, username):
    doc = BeautifulSoup(xml)
    
    result = {}
    
    result['items']    = []
    result['subtotal'] = 0
        
    contracts  = doc.findAll('contrato')
    
    if (len(contracts) < 1):
        print "ERROR: NOT detected contracts!!!"
        return
    
    first_contract = get_value(contracts[0])
    
    # Making sure all contracts match!
    for contract in contracts:
        if (get_value(contract) != first_contract):
            print "ERROR: TOO MANY different contracts!!!"
            return
    
    #TODO: READ user form SDR file
    #result['contract'] = str(first_contract)
    result['contract'] = str(username)
    
    consumptions = doc.findAll('consumo_variable')
    
    for consumption in consumptions:
        concept = str(get_content(consumption, 'concepto_facturable'))
        amount = float(get_content(consumption, 'unidades'))
        
        price = float(get_price(concept))
        description = get_description(concept)
        
        invoiceEntry = createInvoiceEntry(concept, price, description, amount)
        
        result['items'].append(invoiceEntry)
        
        result['subtotal'] += invoiceEntry['total']
    
    # Computing subtotal
    result['total'] = getTax() * result['subtotal']
    
    # Computing subtotal
    result['tax_rate'] = (getTax() - 1) * 100
    
    # Computing taxes
    result['taxes'] = result['total'] - result['subtotal']
    

    
    return result

def getTax():
    return TAX

def createInvoiceEntry(concept, price, description, amount):
    return {
            'concept': unicode(concept), 
            'price': price, 
            'description': unicode(description), 
            'amount': amount, 
            'total': price*amount
            }

def get_value(element):
    return element.string

def get_price(concept):
    if (CATALOGUE.get(concept, -1) == -1):
        print("missing code: " + concept)
        return -1;
        
    return CATALOGUE[concept]['price']

def get_description(concept):
    if (CATALOGUE.get(concept, -1) == -1):
        print("missing code: " + concept)
        return "";
        
    return CATALOGUE[concept]['description']


def get_content(consumption, fieldName):
    return getattr(consumption, fieldName).string