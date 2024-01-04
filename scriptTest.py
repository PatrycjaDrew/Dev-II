import unittest
from tri_points import *


class TestMoyenne(unittest.TestCase):
    def test_moyenneUnSeulPoint(self):
        self.assertEqual(moyenne([10]), 10)
        self.assertEqual(moyenne([0]), 0)

    def  test_moyennePlusieursPoints(self):
        self.assertEqual(moyenne([2,11,5]), 6)
        self.assertEqual(moyenne([0,0,0]), 0)
        self.assertEqual(moyenne([20,20,20,0]), 15)

    def test_moyenneFloat(self):
        self.assertEqual(moyenne([11.1, 18.5]), 14.8)
        self.assertEqual(moyenne([5, 6.7, 10, 8.7]), 7.6)


class TestAjoutDictionnaire(unittest.TestCase):
    def test_ajoutNouvelEleve(self):
        ajout_dictionnaire('Patrycja', 'Drewnowska', '11')
        self.assertEqual(ensemble_eleves, {'Patrycja Drewnowska' : [11.0]})

        ajout_dictionnaire('Patrycja', 'Drewnowska', '15.5')
        self.assertEqual(ensemble_eleves, {'Patrycja Drewnowska': [11.0, 15.5]})


class TestPointsCorrect(unittest.TestCase):
    def test_pointsCorrect(self):
        self.assertTrue(pointsCorrect('6'))
        self.assertTrue(pointsCorrect('0'))
        self.assertTrue(pointsCorrect('10'))
        self.assertTrue(pointsCorrect('20'))

    def test_pointsPasNombre(self):
        self.assertFalse(pointsCorrect('e'))
        self.assertFalse(pointsCorrect('5K'))
        self.assertFalse(pointsCorrect(' '))

    def test_pointsNegatif(self):
        self.assertFalse(pointsCorrect('-40'))
        self.assertFalse(pointsCorrect('-1'))

    def test_pointsTropGrand(self):
        self.assertFalse(pointsCorrect('100'))
        self.assertFalse(pointsCorrect('21'))



if __name__ ==   '__main__':
    unittest.main()
