#!/usr/bin/python
# coding=utf-8 

'''
Created on 30/10/2012

@author: mac
'''

from django.contrib.auth.models import User

from models          import UserProfile 
from wordpay.charger import Charger

from common.form_tools import getData

def createUser(acquireForm):
    username = getData(acquireForm, 'username')
    
    first_name  = getData(acquireForm, 'first_name')
    last_name   = getData(acquireForm, 'last_name')
    email       = getData(acquireForm, 'email')
    
    user = User(username=username, first_name=first_name, 
                last_name=last_name, email=email)
    
    user.save()
    
    return user

def createProfile(acquireForm, charger, user):
    
    title       = getData(acquireForm, 'title')
    
    phone       = getData(acquireForm, 'phone')
    company     = getData(acquireForm, 'company')
    
    address     = getData(acquireForm, 'address')
    postal_code = getData(acquireForm, 'postal_code')
    city        = getData(acquireForm, 'city')
    country     = getData(acquireForm, 'country')
       
    profile = UserProfile(user=user, phone=phone, company=company,
                          order_id=charger.getOrder(), 
                          title=title, address=address,
                          city=city, country=country,
                          postal_code=postal_code)
    profile.save()
    
    return profile

def accessCustomerData(user):
    profile = user.get_profile()
    
    full_name = u'{0} {1}'.format(user.first_name, user.last_name)
    
    data =  {
            'name'       : full_name, 
            'address'    : profile.address, 
            'city'       : profile.city, 
            'postal_code': profile.postal_code, 
            'email'      : user.email,
            'country'    : profile.country,
            'order'      : profile.order_id
            }
    
    return data

def initialPaymentUrl(form):
    # Only WorldPay at the moment
    charger = Charger()
    
    user = createUser(form)
    profile = createProfile(form, charger, user)
    
    url = charger.getRedirectUrl(profile)
    
    return url