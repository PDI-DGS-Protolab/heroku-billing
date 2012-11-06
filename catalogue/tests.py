import unittest

from generator import generateCatalogueFromSalesForce

class TestSalesForce(unittest.TestCase):
    def testGenerateCatalogue(self):
        generateCatalogueFromSalesForce()
        