#!/usr/bin/python
# coding=utf-8 

'''
Created on 16/10/2012

@author: mac
'''

from django.shortcuts           import render
from django.http                import HttpResponseRedirect

from forms    import AcquireForm
from services import initialPaymentUrl

def acquire(request):
    
    if request.method == 'POST': 
        
        form = AcquireForm(request.POST) 
        
        if form.is_valid(): 
                        
            url = initialPaymentUrl(form)
            
            return HttpResponseRedirect(url)
    else:
        form = AcquireForm() 

    return render(request, 'acquire.html', {
        'form': form,
    })
