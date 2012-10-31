import unittest

from tasks    import downloadAndParseSDRTask

from common.aws.s3 import getSDRRequestKeys

class TestDownloadFromS3Case(unittest.TestCase):
    def testDownloadAndParseSDR(self):
        
        json = downloadAndParseSDRTask('sdr.xml')
        
        self.assertEqual(json['total'], float(1266.49))
        
    def testGetSDRRequestKeys(self):
        
        keys = getSDRRequestKeys()
        
        self.assertEqual(keys, ['sdr.xml'])