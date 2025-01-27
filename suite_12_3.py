import unittest
import Unit_test_methods
import simple_unit_test

uttm = unittest.TestSuite()
uttm.addTest(unittest.TestLoader().loadTestsFromTestCase(Unit_test_methods.TournamentTest))
uttm.addTest(unittest.TestLoader().loadTestsFromTestCase(simple_unit_test.RunnerTest))

uttm_runner = unittest.TextTestRunner(verbosity=2)
uttm_runner.run(uttm)
