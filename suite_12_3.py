import unittest
from tests1 import tests_Runner
from tests1 import tests_tournament

testsSt = unittest.TestSuite()
testsSt.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_Runner.RunnerTest))
testsSt.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_tournament.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(testsSt)
