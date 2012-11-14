import os
import unittest

from common.salesforce.salesforce import get_catalogue

os.chdir("..")

class TestSalesForce(unittest.TestCase):
    
    def test_download_catalogue_from_sf(self):
        catalogue_data = get_catalogue()
        
        self.assertTrue(len(catalogue_data['products']) >= 0, "Problem connecting to SalesForce")