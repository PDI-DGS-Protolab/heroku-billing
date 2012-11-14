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

from common.aws.s3 import upload_invoice_to_s3

def compute_invoice_details ():
    return {
            'number': 23,
            'date': date.today(),
            'logo': unicode(LOGO_PATH)
           }

def generate_pdf_and_upload(invoice_json):
    
    # Adding ".pdf" fo the name of the SDR file
    file_name = "{0}.pdf".format(invoice_json['sdr_file_name'])
    
    invoice_json['invoice'] = compute_invoice_details()
    
    pisa.showLogging()
    
    with codecs.open(TEMPLATE_PATH, 'r', 'utf-8') as f:
        template_content = f.read()
        
    template = Template(template_content)
    
    with open (file_name, "wb") as f:
        pdf = pisa.CreatePDF(template.render(invoice_json), f)
    
    if not pdf.err:                             
        upload_invoice_to_s3(file_name)
        
    invoice_json['pdf_file_name'] = file_name

    return invoice_json