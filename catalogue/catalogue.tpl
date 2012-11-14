'''
This is an automatically generated file! Do no edit!

If price changes exists, modify the SF catalogue instead.
'''

TAX = 1.20

CATALOGUE = {}

{% for p in products %}
CATALOGUE['{{ p.code }}'] = {'price': {{ p.price }}, 'description': "{{ p.description }}"}
{% endfor %}


