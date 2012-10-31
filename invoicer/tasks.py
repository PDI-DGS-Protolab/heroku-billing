#!/usr/bin/python
# coding=utf-8 

'''
Created on 15/10/2012

@author: mac
'''

from celery import task
 
from rating.rating     import downloadAndParseSDR
from pdf.invoice       import generatePDFAndUpload
from customer.customer import customerDetails
from email.email       import sendEmail
from charging.charging import charge

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
def sendEmailTask(json):
    return sendEmail(json)

@task(ignore_result=True)
def chargeTask(json):
    return charge(json)

def startProcessFromS3(bucket_key):
    chain = downloadAndParseSDRTask.s(bucket_key) | getCustomerDetailsTask.s() | generatePDFAndUploadTask.s() | sendEmailTask.s() | chargeTask.s()
            
    chain()

def startSyncProcessFromS3(bucket_key):
    json = downloadAndParseSDRTask(bucket_key)
    json = getCustomerDetailsTask(json)
    #json = generatePDFAndUploadTask(json) 
    #json = sendEmailTask(json)
    json = chargeTask(json)