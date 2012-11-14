#!/usr/bin/python
# coding=utf-8 

'''
Created on 15/10/2012

@author: mac
'''

from celery import task
 
from rating.rating       import download_and_parse_sdr
from pdf.invoice         import generate_pdf_and_upload
from customer.localDB    import customer_details
from customer.salesforce import customer_details_from_sf
from email.email         import send_email
from charging.charging   import charge

@task(ignore_result=True)
def download_and_parse_sdr_task(bucket_key):
    return download_and_parse_sdr(bucket_key)

@task(ignore_result=True)
def generate_pdf_and_upload_task(invoiceJson):
    return generate_pdf_and_upload(invoiceJson)

@task(ignore_result=True)
def get_customer_details_task(json):
    return customer_details(json)

@task(ignore_result=True)
def get_customer_details_from_sf_task(json):
    return customer_details_from_sf(json)

@task(ignore_result=True)
def uploadOrderLineToSalesForce(json):
    #TODOOOOO!
    return json

@task(ignore_result=True)
def send_email_task(json):
    return send_email(json)

@task(ignore_result=True)
def charge_task(json):
    return charge(json)

def start_process_from_s3(bucket_key):
    chain = download_and_parse_sdr_task.s(bucket_key) | get_customer_details_task.s() | generate_pdf_and_upload_task.s() | send_email_task.s() | charge_task.s() | uploadOrderLineToSalesForce.s()
            
    chain()

def start_sync_process_from_s3(bucket_key):
    json = download_and_parse_sdr_task(bucket_key)
    json = get_customer_details_task(json)
    json = generate_pdf_and_upload_task(json) 
    json = send_email_task(json)
    json = charge_task(json)