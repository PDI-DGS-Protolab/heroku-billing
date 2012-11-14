'''
Created on 31/10/2012

@author: mac
'''

from payment.wordpay.charger import Charger

def charge(json):

    charger = Charger()
    
    order  = json['customer']['order']
    amount = json['total']

    charger.recurrent_payment(order, amount)
    
    return json