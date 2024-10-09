from unittest import TestCase
from runner import Runner


class RunnerTest(TestCase):
    def test_walk(self):
        r1 = Runner('Сергей')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50, f'{r1.name} прошёл {r1.distance} хотя должен был пройти 50')
    def test_run(self):
        r2 = Runner('Антон')
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100, f'{r2.name} пробежал {r2.distance} хотя должен был пробежать 100')
    def test_challenge(self):
        r1 = Runner('Сергей')
        r2 = Runner('Антон')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)
