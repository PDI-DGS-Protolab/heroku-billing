#!/usr/bin/python
# coding=utf-8 

'''
Created on 30/10/2012

@author: mac
'''

from django.contrib.auth.models import User

from models          import UserProfile 
from wordpay.charger import Charger

from common.form_tools import get_data

def create_user(acquire_form):
    username = get_data(acquire_form, 'username')
    
    first_name  = get_data(acquire_form, 'first_name')
    last_name   = get_data(acquire_form, 'last_name')
    email       = get_data(acquire_form, 'email')
    
    user = User(username=username, first_name=first_name, 
                last_name=last_name, email=email)
    
    user.save()
    
    return user

def create_profile(acquire_form, charger, user):
    
    title       = get_data(acquire_form, 'title')
    
    phone       = get_data(acquire_form, 'phone')
    company     = get_data(acquire_form, 'company')
    
    address     = get_data(acquire_form, 'address')
    postal_code = get_data(acquire_form, 'postal_code')
    city        = get_data(acquire_form, 'city')
    country     = get_data(acquire_form, 'country')
       
    profile = UserProfile(user=user, phone=phone, company=company,
                          order_id=charger.get_order(), 
                          title=title, address=address,
                          city=city, country=country,
                          postal_code=postal_code)
    profile.save()
    
    return profile

def access_customer_data(user):
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

def initial_payment_url(form):
    # Only WorldPay at the moment
    charger = Charger()
    
    user = create_user(form)
    profile = create_profile(form, charger, user)
    
    url = charger.get_redirect_url(profile)
    
    return url