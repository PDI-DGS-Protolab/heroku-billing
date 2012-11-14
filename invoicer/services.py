#!/usr/bin/python
# coding=utf-8 

'''
Created on 16/10/2012

@author: mac
'''

from common.aws.s3 import get_sdr_request_keys
from invoicer.tasks import start_process_from_s3, start_sync_process_from_s3
    
def add_invoice_tasks_from_s3():
    
    keys = get_sdr_request_keys()
    
    for key in keys:
        start_process_from_s3(key)

   
def invoice_1_task_from_s3():
    
    keys = get_sdr_request_keys()
    
    for key in keys:
        start_sync_process_from_s3(key)
        break