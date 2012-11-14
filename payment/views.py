#!/usr/bin/python
# coding=utf-8 

'''
Created on 16/10/2012

@author: mac
'''

from django.shortcuts import render
from django.http      import HttpResponseRedirect
from django.db        import transaction

from forms    import AcquireForm
from services import initial_payment_url

@transaction.commit_on_success
def acquire(request):
    
    if request.method == 'POST': 
        
        form = AcquireForm(request.POST) 
        
        if form.is_valid(): 
                        
            url = initial_payment_url(form)
            
            return HttpResponseRedirect(url)
    else:
        form = AcquireForm() 

    return render(request, 'acquire.html', {
        'form': form,
    })

def success(request):
    return render(request, 'success.html', {})

def pending(request):
    return render(request, 'pending.html', {})

def error(request):
    return render(request, 'error.html', {})
