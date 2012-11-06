'''
Created on 06/11/2012

@author: mac
'''

TAX = 1.20

CATALOGUE = {}

{% for p in products %}
CATALOGUE['{{ p.code }}'] = {'price': {{ p.price }}, 'description': "{{ p.description }}"}
{% endfor %}


