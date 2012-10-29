from django.conf.urls import patterns, url

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'payment.views.acquire'),
    
    url(r'^customers/$', 'payment.views.getCustomers'),
    url(r'^customers/(\w+)/$', 'payment.views.invoice'),
    url(r'^customers/(\w+)/data/$', 'payment.views.getCustomerData'),
    
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}), 
    
    #url(r'^customerDetails/(\d+)/$', 'payment.views.getCustomerDetails'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
