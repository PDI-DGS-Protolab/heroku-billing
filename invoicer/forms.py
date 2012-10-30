'''
Created on 16/10/2012

@author: mac
'''

from django import forms

class InvoiceForm(forms.Form):
    username   = forms.CharField(max_length=30, min_length=3, widget=forms.HiddenInput())
    sdr        = forms.FileField()