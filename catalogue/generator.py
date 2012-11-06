'''
Created on 06/11/2012

@author: mac
'''

from jinja2 import Template

from common.salesforce.salesforce import getCatalogue

import codecs

TEMPLATE_PATH  = "catalogue/catalogue.tpl"
CATALOGUE_PATH = "invoicer/rating/catalogue.py"

def generateCatalogueFromSalesForce():
    
    catalogue = getCatalogue()
    
    with codecs.open(TEMPLATE_PATH, 'r', 'utf-8') as f:
        template_content = f.read()
        
    template = Template(template_content)
    
    with open (CATALOGUE_PATH, "wb") as f:
        f.write(template.render(catalogue))