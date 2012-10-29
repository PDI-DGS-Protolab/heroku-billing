#!/usr/bin/python
# coding=utf-8 

'''
Created on 15/10/2012

@author: mac
'''

from celery import task
 
from rating.rating import parseSDR
from pdf.invoice import generateInvoicePDF
from customer.customer import  customerDetails

from django.core.mail import send_mail

@task(ignore_result=True)
def readSDR(sdr, username):
    return parseSDR(sdr, username)

@task(ignore_result=True)
def generateInvoice(invoiceJson, filename):
    return generateInvoicePDF(invoiceJson, filename)

@task(ignore_result=True)
def getCustomerDetails(json):
    return customerDetails(json)

@task(ignore_result=True)
def sendEmail(json):
    send_mail('Test', 'Su factura', 'macvaz82@gmail.com', ['mac@tid.es'], fail_silently=False)

def executeProcess(xml, username):
    chain = readSDR.s(xml, username) | getCustomerDetails.s() | generateInvoice.s('invoice1.pdf') | sendEmail.s()
    chain()