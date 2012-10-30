import unittest

from tasks    import downloadAndParseSDRTask
from services import addInvoiceTasksFromS3

from common.aws.s3 import getSDRRequestKeys

class TestDownloadFromS3Case(unittest.TestCase):
    def testDownloadAndParseSDR(self):
        
        json = downloadAndParseSDRTask('sdr.xml')
        
        self.assertEqual(json['total'], 1266.4631999999999)
        
    def testGetSDRRequestKeys(self):
        
        keys = getSDRRequestKeys()
        
        self.assertEqual(keys, ['sdr.xml'])
    
    def testAddInvoiceTasksFromS3(self):
        
        return
        addInvoiceTasksFromS3()