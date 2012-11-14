'''
Created on 30/10/2012

@author: mac
'''

def get_data(form, fieldname):
    return form.cleaned_data[fieldname]