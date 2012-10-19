'''
Created on 10/10/2012

@author: mac
'''

TAX = 1.20

CATALOGUE = {}

# OS CATALOGUE, VM PRICES
# Prices are per hour
# SmartOS Plus Catalogue
CATALOGUE['01001'] = {'price': 0.065, 'description': "SmartOSPlus XS 1GB/1CPU/30GB"}
CATALOGUE['02001'] = {'price': 0.131, 'description': "SmartOSPlus S 2GB/1CPU/60GB"}
CATALOGUE['03001'] = {'price': 0.184, 'description': "SmartOSPlus M 4GB/1CPU/120GB"}
CATALOGUE['04001'] = {'price': 0.277, 'description': "SmartOSPlus L 8GB/2CPU/240GB"}
CATALOGUE['05001'] = {'price': 0.492, 'description': "SmartOSPlus XL 16GB/3CPU/480GB"}
# SmartOS Plus 64 Catalogue
CATALOGUE['01002'] = {'price': 0.065, 'description': "SmartOSPlus64 XS 1GB/1CPU/30GB"}
CATALOGUE['02002'] = {'price': 0.131, 'description': "SmartOSPlus64 S 2GB/1CPU/60GB"}
CATALOGUE['03002'] = {'price': 0.184, 'description': "SmartOSPlus64 M 4GB/1CPU/120GB"}
CATALOGUE['04002'] = {'price': 0.277, 'description': "SmartOSPlus64 L 8GB/2CPU/240GB"}
CATALOGUE['05002'] = {'price': 0.492, 'description': "SmartOSPlus64 XL 16GB/3CPU/480GB"}
# SmartOS Catalogue
CATALOGUE['01003'] = {'price': 0.065, 'description': "SmartOS XS 1GB/1CPU/30GB"}
CATALOGUE['02003'] = {'price': 0.131, 'description': "SmartOS S 2GB/1CPU/60GB"}
CATALOGUE['03003'] = {'price': 0.184, 'description': "SmartOS M 4GB/1CPU/120GB"}
CATALOGUE['04003'] = {'price': 0.277, 'description': "SmartOS L 8GB/2CPU/240GB"}
CATALOGUE['05003'] = {'price': 0.492, 'description': "SmartOS XL 16GB/3CPU/480GB"}
# SmartOS64 Catalogue
CATALOGUE['01004'] = {'price': 0.065, 'description': "SmartOS64 XS 1GB/1CPU/30GB"}
CATALOGUE['02004'] = {'price': 0.131, 'description': "SmartOS64 S 2GB/1CPU/60GB"}
CATALOGUE['03004'] = {'price': 0.184, 'description': "SmartOS64 M 4GB/1CPU/120GB"}
CATALOGUE['04004'] = {'price': 0.277, 'description': "SmartOS64 L 8GB/2CPU/240GB"}
CATALOGUE['05004'] = {'price': 0.492, 'description': "SmartOS64 XL 16GB/3CPU/480GB"}
# Windows Server 2008 - Standard
# Note: there are not price for Windows Server 2008 - Standard XS 1GB/1CPU/30GB
#CATALOGUE['01018'] = {'price': 0.149, 'description': "Windows Server 2008 - Standard XS 1GB/1CPU/30GB"}
CATALOGUE['02018'] = {'price': 0.149, 'description': "Windows Server 2008 - Standard S 2GB/1CPU/60GB"}
CATALOGUE['03018'] = {'price': 0.223, 'description': "Windows Server 2008 - Standard M 4GB/1CPU/120GB"}
CATALOGUE['04018'] = {'price': 0.354, 'description': "Windows Server 2008 - Standard L 8GB/2CPU/240GB"}
CATALOGUE['05018'] = {'price': 0.647, 'description': "Windows Server 2008 - Standard XL 16GB/3CPU/480GB"}
# Windows Server 2008 - Enterprise
# Note there are not prices for Windows Server 2008 - enterprise
#CATALOGUE['01019'] = {'price': 0.205, 'description': "Windows Server 2008 - Enterprise XS 1GB/1CPU/30GB"}
CATALOGUE['02019'] = {'price': 0.205, 'description': "Windows Server 2008 - Enterprise S 2GB/1CPU/60GB"}
CATALOGUE['03019'] = {'price': 0.308, 'description': "Windows Server 2008 - Enterprise M 4GB/1CPU/120GB"}
CATALOGUE['04019'] = {'price': 0.523, 'description': "Windows Server 2008 - Enterprise L 8GB/2CPU/240GB"}
CATALOGUE['05019'] = {'price': 0.799, 'description': "Windows Server 2008 - Enterprise XL 16GB/3CPU/480GB"}
# Centos-5.7 Catalogue
CATALOGUE['01013'] = {'price': 0.065, 'description': "Centos-5.7 XS 1GB/1CPU/30GB"}
CATALOGUE['02013'] = {'price': 0.131, 'description': "Centos-5.7 S 2GB/1CPU/60GB"}
CATALOGUE['03013'] = {'price': 0.184, 'description': "Centos-5.7 M 4GB/1CPU/120GB"}
CATALOGUE['04013'] = {'price': 0.277, 'description': "Centos-5.7 L 8GB/2CPU/240GB"}
CATALOGUE['05013'] = {'price': 0.492, 'description': "Centos-5.7 XL 16GB/3CPU/480GB"}
# Centos-6 Catalogue
CATALOGUE['01014'] = {'price': 0.065, 'description': "Centos-5.7 XS 1GB/1CPU/30GB"}
CATALOGUE['02014'] = {'price': 0.131, 'description': "Centos-5.7 S 2GB/1CPU/60GB"}
CATALOGUE['03014'] = {'price': 0.184, 'description': "Centos-5.7 M 4GB/1CPU/120GB"}
CATALOGUE['04014'] = {'price': 0.277, 'description': "Centos-5.7 L 8GB/2CPU/240GB"}
CATALOGUE['05014'] = {'price': 0.492, 'description': "Centos-5.7 XL 16GB/3CPU/480GB"}
# Debian-6.03 Catalogue
CATALOGUE['01015'] = {'price': 0.065, 'description': "Debian-6.03 XS 1GB/1CPU/30GB"}
CATALOGUE['02015'] = {'price': 0.131, 'description': "Debian-6.03 S 2GB/1CPU/60GB"}
CATALOGUE['03015'] = {'price': 0.184, 'description': "Debian-6.03 M 4GB/1CPU/120GB"}
CATALOGUE['04015'] = {'price': 0.277, 'description': "Debian-6.03 L 8GB/2CPU/240GB"}
CATALOGUE['05015'] = {'price': 0.492, 'description': "Debian-6.03 XL 16GB/3CPU/480GB"}
# Fedora-14 Catalogue
CATALOGUE['01016'] = {'price': 0.065, 'description': "Fedora-14 XS 1GB/1CPU/30GB"}
CATALOGUE['02016'] = {'price': 0.131, 'description': "Fedora-14 S 2GB/1CPU/60GB"}
CATALOGUE['03016'] = {'price': 0.184, 'description': "Fedora-14 M 4GB/1CPU/120GB"}
CATALOGUE['04016'] = {'price': 0.277, 'description': "Fedora-14 L 8GB/2CPU/240GB"}
CATALOGUE['05016'] = {'price': 0.492, 'description': "Fedora-14 XL 16GB/3CPU/480GB"}
# Ubuntu-10.04 Catalogue
CATALOGUE['01017'] = {'price': 0.065, 'description': "Ubuntu-10.04 XS 1GB/1CPU/30GB"}
CATALOGUE['02017'] = {'price': 0.131, 'description': "Ubuntu-10.04 S 2GB/1CPU/60GB"}
CATALOGUE['03017'] = {'price': 0.184, 'description': "Ubuntu-10.04 M 4GB/1CPU/120GB"}
CATALOGUE['04017'] = {'price': 0.277, 'description': "Ubuntu-10.04 L 8GB/2CPU/240GB"}
CATALOGUE['05017'] = {'price': 0.492, 'description': "Ubuntu-10.04 XL 16GB/3CPU/480GB"}
# APP CATALOGUE, VM PRICES
# Prices are per hour
# MongoDB
CATALOGUE['01005'] = {'price': 0.065, 'description': "mongodb-1.2.4 XS 1GB"}
CATALOGUE['02005'] = {'price': 0.131, 'description': "mongodb-1.2.4 S 2GB"}
CATALOGUE['03005'] = {'price': 0.184, 'description': "mongodb-1.2.4 M 4GB"}
CATALOGUE['04005'] = {'price': 0.277, 'description': "mongodb-1.2.4 L 8GB"}
CATALOGUE['05005'] = {'price': 0.492, 'description': "mongodb-1.2.4 XL 16GB"}
# mysql-1.4.1
CATALOGUE['01006'] = {'price': 0.065, 'description': "mysql-1.4.1 XS 1GB"}
CATALOGUE['02006'] = {'price': 0.131, 'description': "mysql-1.4.1 S 2GB"}
CATALOGUE['03006'] = {'price': 0.184, 'description': "mysql-1.4.1 M 4GB"}
CATALOGUE['04006'] = {'price': 0.277, 'description': "mysql-1.4.1 L 8GB"}
CATALOGUE['05006'] = {'price': 0.492, 'description': "mysql-1.4.1 XL 16GB"}
# nodejs-1.3.3
CATALOGUE['01007'] = {'price': 0.065, 'description': "nodejs-1.3.3 XS 1GB"}
CATALOGUE['02007'] = {'price': 0.131, 'description': "nodejs-1.3.3 S 2GB"}
CATALOGUE['03007'] = {'price': 0.184, 'description': "nodejs-1.3.3 M 4GB"}
CATALOGUE['04007'] = {'price': 0.277, 'description': "nodejs-1.3.3 L 8GB"}
CATALOGUE['05007'] = {'price': 0.492, 'description': "nodejs-1.3.3 XL 16GB"}
# riak-1.6.0
CATALOGUE['01008'] = {'price': 0.065, 'description': "riak-1.6.0 XS 1GB"}
CATALOGUE['02008'] = {'price': 0.131, 'description': "riak-1.6.0 S 2GB"}
CATALOGUE['03008'] = {'price': 0.184, 'description': "riak-1.6.0 M 4GB"}
CATALOGUE['04008'] = {'price': 0.277, 'description': "riak-1.6.0 L 8GB"}
CATALOGUE['05008'] = {'price': 0.492, 'description': "riak-1.6.0 XL 16GB"}
# Riakeds
#Note : No price list for Riackeds
#CATALOGUE['01009'] = {'price': 0.065, 'description': "Riakeds XS 1GB"}
#CATALOGUE['02009'] = {'price': 0.131, 'description': "Riakeds S 2GB"}
#CATALOGUE['03009'] = {'price': 0.184, 'description': "Riakeds M 4GB"}
#CATALOGUE['04009'] = {'price': 0.277, 'description': "Riakeds L 8GB"}
#CATALOGUE['05009'] = {'price': 0.492, 'description': "Riakeds XL 16GB"}


