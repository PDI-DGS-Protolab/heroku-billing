'''
Created on 30/10/2012

@author: mac
'''

def getData(form, fieldname):
    return form.cleaned_data[fieldname]