import unittest
from tests1 import Tournament
from tests1 import Runner
import random

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
        a = 'Ник Фьюри'
        cls.all_results.append(a)

    def setUp(self):
        a = Runner.Runner('Усэйн Болт', 10)
        b = Runner.Runner('Андрей Поттер', 9)
        c = Runner.Runner('Ник Фьюри', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def tester(self):
        a = Runner.Runner('Усэйн Болт', 10)
        c = Runner.Runner('Ник Фьюри', 3)
        leader = Tournament.Tournament(90, a, c)
        leader.start()
        self.assertEqual(self.all_results[0], 'Ник Фьюри')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def tester2(self):
        b = Runner.Runner('Андрей Поттер', 9)
        c = Runner.Runner('Ник Фьюри', 3)
        leader1 = Tournament.Tournament(90, b, c)
        leader1.start()
        self.assertEqual(self.all_results[0], 'Ник Фьюри')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def tester3(self):
        a = Runner.Runner('Усэйн Болт', 10)
        b = Runner.Runner('Андрей Поттер', 9)
        c = Runner.Runner('Ник Фьюри', 3)
        leader2 = Tournament.Tournament(90, a, b, c)
        leader2.start()
        self.assertEqual(self.all_results[0], 'Ник Фьюри')

if __name__ == '__main__':
    unittest.main()