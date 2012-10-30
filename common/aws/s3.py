#!/usr/bin/python
# coding=utf-8 

'''
Created on 30/10/2012

@author: mac
'''



from boto.s3.connection import S3Connection
from boto.s3.key        import Key

from constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, SDR_REQUESTS_BUCKET, PDF_INVOICES_BUCKET

def connect():
    return S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

def getSDRRequestKeys():
    conn = connect()
    
    bucket = conn.get_bucket(SDR_REQUESTS_BUCKET)

    rs = bucket.list()
    
    keys = []
    
    for key in rs:
        keys.append(key.name)
    
    return keys

def getBucketKeyContent(key_name):
    
    conn = connect()
    
    bucket = conn.get_bucket(SDR_REQUESTS_BUCKET)
    
    key = bucket.lookup(key_name)
    
    return key.get_contents_as_string()

def uploadInvoiceToS3(file_name):
    conn = connect()
    
    bucket = conn.get_bucket(PDF_INVOICES_BUCKET)
    
    key = Key(bucket)
    
    key.name = file_name
    key.set_contents_from_filename(file_name)
    