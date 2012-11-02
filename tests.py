import unittest

from invoicer.customer.salesforce import getCatalogue

class TestSalesForce(unittest.TestCase):
    def testDownloadCatalogue(self):
        getCatalogue()
        