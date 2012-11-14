'''
Created on 17/10/2012

@author: mac
'''

import uuid

class PaymentGateway:
    
    def get_redirect_rrl(self, profile):
        pass

    def recurrent_payment(self, lastOrder, total):
        pass

    def get_order(self):
        return self.order
    
    def compute_order_id(self):
        uid = uuid.uuid4()
        
        # Order = ten first characters of uuid
        return uid.hex[:10]