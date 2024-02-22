import unittest
import sys

sys.path.append('test')

import flush
import straight
import onepair
import twopairs
import triple
import quadruple
import highest
import fullhouse

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: python test.py TEST_CLASS")
        sys.exit()
        
    testSuites = [
        highest.TestHighest,
        onepair.TestOnePair, 
        twopairs.TestTwoPairs, 
        triple.TestTriple, 
        straight.TestStraight, 
        flush.TestFlush, 
        fullhouse.TestFullhouse,
        quadruple.TestQuadruple
    ]
    
    if sys.argv[1] in ['flush', 'Flush']:
        testSuite = flush.TestFlush
    elif sys.argv[1] in ['straight', 'Straight']:
        testSuite = straight.TestStraight
    elif sys.argv[1] in ['onepair', 'Pair', 'pair']:
        testSuite = onepair.TestOnePair
    elif sys.argv[1] in ['twopairs', 'twopair']:
        testSuite = twopairs.TestTwoPairs
    elif sys.argv[1] in ['triple', 'threeofakind']:
        testSuite = triple.TestTriple
    elif sys.argv[1] in ['quadruple', 'quad', 'fourofakind']:
        testSuite = quadruple.TestQuadruple
    elif sys.argv[1] in ['highest', 'one']:
        testSuite = highest.TestHighest
    elif sys.argv[1] in ['fullhouse']:
        testSuite = fullhouse.TestFullhouse
        
    elif sys.argv[1] == 'all':
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        for testSuite in testSuites:
            suite.addTests(loader.loadTestsFromTestCase(testSuite))
            
        unittest.TextTestRunner(verbosity=2).run(suite)
        sys.exit()
    else:
        print("No suite detected")
        print("Usage: python test.py TEST_CLASS")
        sys.exit()
        
        
    unittest.main(verbosity=3, testRunner=unittest.TextTestRunner()).run(unittest.TestLoader().loadTestsFromTestCase(testSuite))
