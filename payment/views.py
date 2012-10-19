#!/usr/bin/python
# coding=utf-8 

'''
Created on 16/10/2012

@author: mac
'''

from django.shortcuts           import render
from django.http                import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from payment.forms  import AcquireForm, InvoiceForm
from payment.models import UserProfile 

from wordpay.charger import Charger

from invoicer.rating.rating import parseSDR
from invoicer.pdf.invoice import generateInvoicePDF
from invoicer.customer.customer import customerDetails

import json

def acquire(request):
    
    if request.method == 'POST': 
        
        form = AcquireForm(request.POST) 
        
        if form.is_valid(): 
            
            # Only WorldPay at the moment
            charger = Charger()
            
            user = createUser(form)
            profile = createProfile(form, charger, user)
            
            url = charger.getRedirectUrl(profile)
            
            return HttpResponseRedirect(url)
    else:
        form = AcquireForm() 

    return render(request, 'acquire.html', {
        'form': form,
    })

def invoice(request, username):
    
    if request.method == 'POST': 
        
        form = InvoiceForm(request.POST, request.FILES) 
        
        if form.is_valid(): 
            return generatePDF(request.FILES['sdr'], getData(form, 'username'))
    else:
        form = InvoiceForm(initial = {"username": username}) 

    return render(request, 'invoice_user.html', {
        'form': form,
        'username': username,
    })
    
def generatePDF(sdrContent, username):
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    
    json = parseSDR(sdrContent, username)
    json = customerDetails(json)
    generateInvoicePDF(json, 'invoice.pdf')
    
    with open("invoice.pdf", 'r') as f:
        pdfContent = f.read()
    
    response.write(pdfContent)
    
    return response
    
def getCustomers(request):
    
    users = User.objects.filter(is_superuser=False)
    
    return render(request, 'list_users.html', {
        'users': users,
    })
    
def invoiceCustomer(request, username):
    users = User.objects.filter(username=username)
    
    if (len(users) != 1):
        return HttpResponse(json.dumps({}), mimetype="application/json")
    
    user = users[0]
    
    return render(request, 'invoice_user.html', {
        'user': user,
    }) 

def getCustomerData(request, username):
    
    users = User.objects.filter(username=username)
    
    if (len(users) != 1):
        return HttpResponse(json.dumps({}), mimetype="application/json")
    
    user = users[0]
    
    data = accessCustomerData(user)
    
    return HttpResponse(json.dumps(data), mimetype="application/json")

def accessCustomerData(user):
    profile = user.get_profile()
    
    full_name = u'{0} {1}'.format(user.first_name, user.last_name)
    
    data =  {
            'name'       : full_name, 
            'address'    : profile.address, 
            'city'       : profile.city, 
            'postal_code': profile.postal_code, 
            'email'      : user.email,
            'country'    : profile.country
            }
    
    return data

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

def getData(form, fieldname):
    return form.cleaned_data[fieldname]