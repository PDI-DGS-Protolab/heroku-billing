'''
Created on 17/10/2012

@author: mac
'''

from payment.wordpay.charger import Charger

charger = Charger()

charger.recurrentPayment("aa9b5184ed", 20000)