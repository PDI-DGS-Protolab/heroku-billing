#!/usr/bin/python
# coding=utf-8 

'''
Created on 30/10/2012

@author: mac
'''

from django.shortcuts           import render

from services import addInvoiceTasksFromS3, invoice1TaskFromS3

def launchInvoice(request):
    
    addInvoiceTasksFromS3()
    
    return render(request, 'invoicing.html', {})

def launchSyncInvoice(request):
    
    invoice1TaskFromS3()
    
    return render(request, 'invoicing.html', {})
    
