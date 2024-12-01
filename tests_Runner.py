import unittest
from tests1 import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen == True, "Frozen test")
    def test_walk(self):
        runner = Runner.Runner('<NAME>')
        for i in range(10):
            runner.walk()
            runner_distance = runner.distance
        self.assertEqual(runner_distance, 50)

    @unittest.skipIf(is_frozen == True, "Frozen test")
    def test_run(self):
        runner1 = Runner.Runner('<NAME1>')
        for i in range(10):
            runner1.run()
            runner1_distance = runner1.distance
        self.assertEqual(runner1_distance, 100)

    @unittest.skipIf(is_frozen == True, "Frozen test")
    def test_challenge(self):
        runner2 = Runner.Runner('<NAME2>')
        runner3 = Runner.Runner('<NAME3>')
        for i in range(10):
            runner2.run()
            runner2_distance = runner2.distance
        for i in range(10):
            runner3.walk()
            runner3_distance = runner3.distance
        self.assertNotEqual(runner2_distance, runner3_distance)

if __name__ == '__main__':
    unittest.main()
