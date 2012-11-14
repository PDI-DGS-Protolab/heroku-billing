from django.utils import unittest

from test1_sdr import XML
from catalogue import CATALOGUE, TAX

from invoicer.rating.rating import parse_sdr

class TestSdrs(unittest.TestCase):
    
    file_name = 'test1'
    
    def test_test1_sdr(self):
        
        data = parse_sdr(XML, self.file_name, CATALOGUE, TAX)
        
        self.assertEqual(data['total'],         float(1365.25))
        self.assertEqual(data['sdr_file_name'], self.file_name)