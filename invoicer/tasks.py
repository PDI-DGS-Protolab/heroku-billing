#!/usr/bin/python
# coding=utf-8 

'''
Created on 15/10/2012

@author: mac
'''

from celery import task
 
from rating.rating       import downloadAndParseSDR
from pdf.invoice         import generatePDFAndUpload
from customer.localDB    import customerDetails
from customer.salesforce import customerDetailsFromSF
from email.email         import sendEmail
from charging.charging   import charge

@task(ignore_result=True)
def downloadAndParseSDRTask(bucket_key):
    return downloadAndParseSDR(bucket_key)

@task(ignore_result=True)
def generatePDFAndUploadTask(invoiceJson):
    return generatePDFAndUpload(invoiceJson)

@task(ignore_result=True)
def getCustomerDetailsTask(json):
    return customerDetails(json)

@task(ignore_result=True)
def getCustomerDetailsFromSalesForceTask(json):
    return customerDetailsFromSF(json)

@task(ignore_result=True)
def uploadOrderLineToSalesForce(json):
    #TODOOOOO!
    return json

@task(ignore_result=True)
def sendEmailTask(json):
    return sendEmail(json)

@task(ignore_result=True)
def chargeTask(json):
    return charge(json)

def startProcessFromS3(bucket_key):
    chain = downloadAndParseSDRTask.s(bucket_key) | getCustomerDetailsFromSalesForceTask.s() | generatePDFAndUploadTask.s() | sendEmailTask.s() | chargeTask.s() | uploadOrderLineToSalesForce.s()
            
    chain()

def startSyncProcessFromS3(bucket_key):
    json = downloadAndParseSDRTask(bucket_key)
    json = getCustomerDetailsFromSalesForceTask(json)
    json = generatePDFAndUploadTask(json) 
    json = sendEmailTask(json)
    json = chargeTask(json)