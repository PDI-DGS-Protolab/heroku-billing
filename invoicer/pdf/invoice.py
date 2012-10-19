#!/usr/bin/python
# coding=utf-8 

'''
Created on 10/10/2012

@author: mac
'''

from xhtml2pdf import pisa
from jinja2 import Template
from datetime import date

TEMPLATE_PATH = 'invoicer/pdf/template/invoice.html'
LOGO_PATH     = 'invoicer/pdf/template/logo.png'

import codecs

def computeInvoiceDetails ():
    return {
            'number': 23,
            'date': date.today(),
            'logo': unicode(LOGO_PATH)
           }

def generateInvoicePDF(invoice_json, file_name):
    
    invoice_json['invoice'] = computeInvoiceDetails()
    
    pisa.showLogging()
    
    with codecs.open(TEMPLATE_PATH, 'r', 'utf-8') as f:
        template_content = f.read()
        
    template = Template(template_content)
    
    with open (file_name, "wb") as f:
        pdf = pisa.CreatePDF(template.render(invoice_json), f)
    
    if not pdf.err:                             
        pisa.startViewer(file_name)  

