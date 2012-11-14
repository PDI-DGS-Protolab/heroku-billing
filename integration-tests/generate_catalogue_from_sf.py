import unittest

import os
import time

from catalogue.generator import generate_catalogue_from_sf, CATALOGUE_PATH

os.chdir("..")

class TestGenerator(unittest.TestCase):
    
    def test_modification_time(self):
        
        before = time.time()
        
        generate_catalogue_from_sf()
        
        # Reading modification tiemstamp of the file
        modified_time = os.path.getmtime(CATALOGUE_PATH)
                                           
        self.assertTrue(before <= modified_time, "The catalogue file should be modified after running this test")