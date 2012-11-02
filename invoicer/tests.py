import unittest

from tasks    import downloadAndParseSDRTask

from common.aws.s3 import getSDRRequestKeys

class TestDownloadFromS3Case(unittest.TestCase):
    def testDownloadAndParseSDR(self):
        
        json = downloadAndParseSDRTask('salesforce.macvaz82.xml')
        
        self.assertEqual(json['total'], float(1266.49))
        
    def testGetSDRRequestKeys(self):
        
        keys = getSDRRequestKeys()
        
        self.assertEqual(keys, ['salesforce.macvaz82.xml'])