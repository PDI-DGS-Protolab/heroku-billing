#!/usr/bin/python
# coding=utf-8 

'''
Created on 16/10/2012

@author: mac
'''

from common.aws.s3 import getSDRRequestKeys
from invoicer.tasks import startProcessFromS3, startSyncProcessFromS3
    
def addInvoiceTasksFromS3():
    
    keys = getSDRRequestKeys()
    
    for key in keys:
        startProcessFromS3(key)

   
def invoice1TaskFromS3():
    
    keys = getSDRRequestKeys()
    
    for key in keys:
        startSyncProcessFromS3(key)
        break