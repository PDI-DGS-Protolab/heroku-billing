from django.conf.urls import patterns, url

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'payment.views.acquire'),
    
    url(r'^success$', 'payment.views.success'),
    url(r'^pending$', 'payment.views.pending'),
    url(r'^error$',   'payment.views.error'),
    
    url(r'^launchInvoice/$',        'invoicer.views.launchInvoice'),
    url(r'^launchSyncInvoice/$',    'invoicer.views.launchSyncInvoice'),
    
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}), 
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
