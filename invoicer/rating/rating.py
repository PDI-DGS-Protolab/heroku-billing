#!/usr/bin/python
# coding=utf-8 

'''
Created on 10/10/2012

@author: mac
'''

from BeautifulSoup import BeautifulSoup

from common.aws.s3 import get_bucket_key_content

from catalogue import CATALOGUE, TAX

def round_price(price):
    return round(price*100)/100

def download_and_parse_sdr(bucket_key):
    xml = get_bucket_key_content(bucket_key)
    
    return parse_sdr(xml, bucket_key, CATALOGUE, TAX)

def parse_sdr(xml, file_name, catalogue, tax):
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
    
    result['contract'] = str(first_contract)
    
    consumptions = doc.findAll('consumo_variable')
    
    for consumption in consumptions:
        concept = str(get_content(consumption, 'concepto_facturable'))
        amount = float(get_content(consumption, 'unidades'))
        
        price = float(get_price(catalogue, concept))
        description = get_description(catalogue, concept)
        
        invoice_entry = create_invoice_entry(concept, price, description, amount)
        
        result['items'].append(invoice_entry)
        
        result['subtotal'] += invoice_entry['total']
    
    # Computing subtotal
    result['total'] = round_price(tax * result['subtotal'])
    
    # Computing subtotal
    result['tax_rate'] = (tax - 1) * 100
    
    # Computing taxes
    result['taxes'] = round_price(result['total'] - result['subtotal'])
    
    # Adding file_name for naming PDF
    result['sdr_file_name'] = file_name
    
    return result

def create_invoice_entry(concept, price, description, amount):
    return {
            'concept': unicode(concept), 
            'price': price, 
            'description': unicode(description), 
            'amount': amount, 
            'total': round_price(price*amount)
            }

def get_value(element):
    return element.string

def get_price(catalogue, concept):
    if (catalogue.get(concept, -1) == -1):
        print("missing code: " + concept)
        return -1
        
    return catalogue[concept]['price']

def get_description(catalogue, concept):
    if (catalogue.get(concept, -1) == -1):
        print("missing code: " + concept)
        return ""
        
    return catalogue[concept]['description']


def get_content(consumption, fieldName):
    data = getattr(consumption, fieldName)
    
    if (not data):
        print("missing field: " + fieldName)
        return ""

    return data.string