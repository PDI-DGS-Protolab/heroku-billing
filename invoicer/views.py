#!/usr/bin/python
# coding=utf-8 

'''
Created on 30/10/2012

@author: mac
'''

from django.shortcuts import render
from django.db        import transaction

from services import add_invoice_tasks_from_s3, invoice_1_task_from_s3

@transaction.commit_on_success
def launchInvoice(request):
    
    add_invoice_tasks_from_s3()
    
    return render(request, 'invoicing.html', {})

@transaction.commit_on_success
def launchSyncInvoice(request):
    
    invoice_1_task_from_s3()
    
    return render(request, 'invoicing.html', {})
    
