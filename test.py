import unittest
import sys

sys.path.append('test')

import flush
import straight
import onepair
import twopairs

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: python test.py TEST_CLASS")
        sys.exit()
    
    if sys.argv[1] in ['flush', 'Flush']:
        testSuite = flush.TestFlush
    elif sys.argv[1] in ['straight', 'Straight']:
        testSuite = straight.TestStraight
    elif sys.argv[1] in ['onepair', 'Pair', 'pair', '1pair']:
        testSuite = onepair.TestOnePair
    elif sys.argv[1] in ['twopairs', 'twopair', '2pair', '2pairs']:
        testSuite = twopairs.TestTwoPairs
        
    unittest.main(verbosity=3, testRunner=unittest.TextTestRunner()).run(unittest.TestLoader().loadTestsFromTestCase(testSuite))
